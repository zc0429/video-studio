import importlib.util
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('verify',ROOT/'.agents/skills/video-production-director/scripts/verify_video.py')
verify=importlib.util.module_from_spec(spec);spec.loader.exec_module(verify)

class FrameTimingTests(unittest.TestCase):
    def test_uniform_60fps_timestamps(self):
        frames=[{'best_effort_timestamp_time':str(4+i/60)} for i in range(60)]
        self.assertTrue(verify.check_frame_timing(frames,60)['constant'])
    def test_same_count_and_average_do_not_hide_irregular_spacing(self):
        times=[i/60 for i in range(60)];times[15]+=0.006
        result=verify.check_frame_timing([{'pts_time':str(t)} for t in times],60)
        self.assertFalse(result['constant'])
    def test_time_base_quantization_is_allowed(self):
        frames=[{'pts_time':f'{i/60:.3f}'} for i in range(60)]
        self.assertTrue(verify.check_frame_timing(frames,60,'1/1000')['constant'])
    def test_missing_and_repeated_timestamps_are_rejected(self):
        self.assertFalse(verify.check_frame_timing([{},{}],60)['constant'])
        self.assertFalse(verify.check_frame_timing([{'pts_time':'0'},{'pts_time':'0'}],60)['constant'])

@unittest.skipUnless(shutil.which('ffmpeg') and shutil.which('ffprobe'),'requires FFmpeg/ffprobe')
class ActualVideoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp=tempfile.TemporaryDirectory();cls.root=Path(cls.tmp.name)
        for fps in [30,60]:
            cmd=['ffmpeg','-hide_banner','-loglevel','error','-y','-f','lavfi','-i',f'testsrc2=size=160x90:rate={fps}:duration=1','-f','lavfi','-i','anullsrc=r=48000:cl=stereo','-t','1','-c:v','libx264','-preset','ultrafast','-pix_fmt','yuv420p','-c:a','aac',str(cls.root/f'{fps}.mp4')]
            subprocess.run(cmd,check=True,capture_output=True)
    @classmethod
    def tearDownClass(cls):cls.tmp.cleanup()
    def project(self):return {'format':{'width':160,'height':90,'fps':60,'frame_rate_mode':'cfr','duration_s':1},'audio':{'required':True}}
    def test_60fps_file_passes_timestamps_frames_audio_and_decode(self):
        result=verify.inspect_video(self.root/'60.mp4',self.project(),True)
        self.assertTrue(result['passed'],result);self.assertEqual(result['read_frames'],60)
        self.assertTrue(result['frame_timing']['constant']);self.assertFalse(result['native_source_fps_verified'])
    def test_30fps_file_does_not_satisfy_60fps_contract(self):
        result=verify.inspect_video(self.root/'30.mp4',self.project())
        self.assertFalse(result['passed']);self.assertIn('output frame rate mismatch',result['errors'])
    def test_missing_required_audio_is_reported(self):
        silent=self.root/'silent.mp4'
        subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',str(self.root/'60.mp4'),'-an','-c:v','copy',str(silent)],check=True,capture_output=True)
        result=verify.inspect_video(silent,self.project())
        self.assertFalse(result['passed']);self.assertIn('required audio stream is missing',result['errors'])

if __name__=='__main__':unittest.main()
