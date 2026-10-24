#!/usr/bin/env python3
"""Offline descriptive metrics for one account. No scraping, forecasts or causal claims."""
import argparse
import csv
import json
import math
from datetime import datetime
from pathlib import Path

COUNTS = ('plays', 'shares', 'saves', 'new_follows', 'qualified_leads')
MONEY = ('settled_receipts', 'refunds', 'cash_cost', 'labor_rate')
NUMBERS = COUNTS + MONEY + ('labor_hours',)
SCOPES = {'organic', 'paid', 'blended', 'unknown'}


def analyze(rows):
    output, errors, warnings, seen, groups = [], [], [], set(), set()
    for index, row in enumerate(rows, 2):
        label = f'CSV line {index}'
        try:
            required = ('video_id', 'observed_at', 'window_h', 'traffic_scope', 'metric_basis')
            for key in required:
                if not str(row.get(key) or '').strip():
                    raise ValueError(f'missing {key}')
            timestamp = datetime.fromisoformat(row['observed_at'].replace('Z', '+00:00'))
            if timestamp.tzinfo is None:
                raise ValueError('observed_at needs a timezone')
            window = float(row['window_h'])
            if not math.isfinite(window) or window <= 0:
                raise ValueError('window_h must be finite and positive')
            scope = row['traffic_scope']
            if scope not in SCOPES:
                raise ValueError('unknown traffic_scope; use organic, paid, blended or unknown')
            values = {}
            for key in NUMBERS:
                raw = str(row.get(key) if row.get(key) is not None else '').strip()
                value = None if raw == '' else float(raw)
                if value is not None and (not math.isfinite(value) or value < 0):
                    raise ValueError(f'{key} must be finite and nonnegative or empty')
                if key in COUNTS and value is not None and not value.is_integer():
                    raise ValueError(f'{key} must be an integer count')
                values[key] = value
            currency = str(row.get('currency') or '').strip()
            if any(values[key] is not None for key in MONEY) and not currency:
                raise ValueError('currency is required for monetary values')
            identity = (row['video_id'], timestamp.isoformat(), window, scope, row['metric_basis'])
            if identity in seen:
                raise ValueError('duplicate snapshot')
            seen.add(identity)
            group = (window, scope, row['metric_basis'], currency)
            groups.add(group)
            plays = values['plays']
            per_1000 = {
                key: (None if plays is None or plays == 0 or values[key] is None
                      else round(values[key] / plays * 1000, 6))
                for key in ('shares', 'saves', 'new_follows', 'qualified_leads')
            }
            components = [values[key] for key in ('settled_receipts', 'refunds', 'cash_cost')]
            cash = None if any(value is None for value in components) else components[0] - components[1] - components[2]
            hours, rate = values['labor_hours'], values['labor_rate']
            adjusted = None if cash is None or hours is None or rate is None else cash - hours * rate
            output.append({
                'video_id': row['video_id'], 'observed_at': row['observed_at'],
                'comparison_group': list(group), 'source_values': values,
                'events_per_1000_plays': per_1000,
                'cash_contribution': None if cash is None else round(cash, 6),
                'labor_adjusted_contribution': None if adjusted is None else round(adjusted, 6),
                'currency': currency or None,
            })
        except (ValueError, TypeError, OverflowError) as exc:
            errors.append(f'{label}: {exc}')
    if len(groups) > 1:
        warnings.append('Different windows/scopes/definitions/currencies: do not compare across comparison_group values.')
    if len({r['video_id'] for r in output}) < len(output):
        warnings.append('Repeated videos have multiple observations: never sum cumulative snapshots.')
    if not rows:
        warnings.append('No observations; this file is an empty template, not a performance record.')
    return {
        'passed': not errors, 'rows': output, 'errors': errors, 'warnings': warnings,
        'limits': 'Descriptive only. Missing remains null. Per-play counts are not user probabilities. No causal, viral, profit-audit or income prediction claim. Verify source mapping and attribution manually.',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('csv_file', type=Path)
    args = parser.parse_args()
    try:
        with args.csv_file.open(encoding='utf-8-sig', newline='') as stream:
            reader = csv.DictReader(stream)
            expected = set(('video_id', 'observed_at', 'window_h', 'traffic_scope', 'metric_basis', 'currency') + NUMBERS)
            if not expected.issubset(set(reader.fieldnames or [])):
                raise ValueError('CSV header does not match METRICS.csv template')
            result = analyze(list(reader))
    except (OSError, ValueError, csv.Error) as exc:
        result = {'passed': False, 'errors': [str(exc)]}
    print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
    return 0 if result['passed'] else 2


if __name__ == '__main__':
    raise SystemExit(main())
