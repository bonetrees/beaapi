import unittest
import beaapi


class TestThrottling(unittest.TestCase):
    def setUp(self):
        # Get key from unversioned file
        import os
        from dotenv import load_dotenv
        load_dotenv()
        self.beakey = os.environ.get("beakey")

    def test_rate_throttling(self):        
        for _ in range(beaapi.MAX_REQUESTS_PER_MINUTE+1):
            beaapi.get_data_set_list(self.beakey)

        self.assertTrue(True)  # So it's marked as a test. Probably there's better way


if __name__ == '__main__':
    unittest.main()
