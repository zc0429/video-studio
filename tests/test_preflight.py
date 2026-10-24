import copy,importlib.util,json,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(name):
    p=ROOT/'.agents/skills/video-production-director/scripts'/f'{name}.py';s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
pf=load('preflight');np=load('new_project')
class PreflightTests(unittest.TestCase):
    def setUp(self):self.p=json.loads((ROOT/'examples/a-bowl/project.json').read_text())
    def check_error(self,p,part,phase=None):
        r=pf.check_project(p,phase);self.assertFalse(r['passed']);self.assertTrue(any(part in e for e in r['errors']),r)
    def authorize(self):
        for a in self.p['approvals'].values():a.update(status='delegated',basis='Test fixture: explicit delegated creative decisions')
    def test_development_is_valid_without_fabricated_approvals(self):self.assertTrue(pf.check_project(self.p)['passed'])
    def test_production_requires_real_record(self):self.check_error(self.p,'not ready','production')
    def test_delegated_authorization_does_not_require_repeat_confirmation(self):
        self.authorize();self.assertTrue(pf.check_project(self.p,'production')['passed'])
    def test_timeline_gap_is_rejected(self):
        self.p['shots'][1]['start_s']=8;self.check_error(self.p,'gap or overlap')
    def test_missing_story_premise(self):
        self.p['brief']['premise']='';self.check_error(self.p,'premise')
    def test_24_to_60_does_not_pass_native_claim(self):
        self.p['format'].update(fps=60,native_fps_claim=True);self.p['shots'][0].update(method='generative',source_fps=24);self.check_error(self.p,'source cadence')
    def test_blind_retry_without_diagnosis(self):
        self.p['shots'][0]['trials']=[{'hypothesis':'reduce deformation','changed_variable':'motion strength','result':'fail'}];self.check_error(self.p,'no diagnosis')
    def test_trial_limit_override_must_be_recorded(self):
        s=self.p['shots'][0];s['trials']=[{'hypothesis':'test camera','changed_variable':'camera','result':'pass'}]*3;self.check_error(self.p,'trial limit');s['trial_limit_override_reason']='User authorized three controlled alternatives';self.assertTrue(pf.check_project(self.p)['passed'])
    def test_paid_job_needs_budget(self):
        self.authorize();self.p['generation'].update(enabled=True,requires_paid_jobs=True);self.check_error(self.p,'no authorized budget','production')
    def test_approval_without_basis_is_not_accepted(self):
        self.p['approvals']['script']['status']='approved';self.check_error(self.p,'no recorded basis')
    def test_scaffold_preserves_existing_work(self):
        with tempfile.TemporaryDirectory() as t:
            target=Path(t)/'project';np.create_project(target);marker=target/'personal.txt';marker.write_text('keep')
            with self.assertRaises(ValueError):np.create_project(target)
            self.assertEqual(marker.read_text(),'keep')
if __name__=='__main__':unittest.main()
