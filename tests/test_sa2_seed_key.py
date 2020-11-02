import unittest
from sa2_seed_key.sa2_seed_key import Sa2SeedKey

class TestSa2SeedKey(unittest.TestCase):
  def test_security(self):
    vs = Sa2SeedKey([0x68, 0x02, 0x81, 0x49, 0x93, 0xa5, 0x5a, 0x55, 0xaa, 0x4a, 0x05, 0x87, 0x81, 0x05, 0x95, 0x26, 0x68, 0x05, 0x82, 0x49, 0x84, 0x5a, 0xa5, 0xaa, 0x55, 0x87, 0x03, 0xf7, 0x80, 0x6a, 0x4c], 0x1a1b1c1d)
    self.assertEqual(vs.execute(), 0x6a37f02e)
    vs = Sa2SeedKey([0x68, 0x02, 0x81, 0x4A, 0x10, 0x68, 0x04, 0x93, 0x08, 0x08, 0x20, 0x09, 0x4A, 0x05, 0x87, 0x22, 0x12, 0x19, 0x54, 0x82, 0x49, 0x93, 0x07, 0x12, 0x20, 0x11, 0x82, 0x4A, 0x05, 0x87, 0x03, 0x11, 0x20, 0x10, 0x82, 0x4A, 0x01, 0x81, 0x49, 0x4C], 0xa04eb1ed)
    res = vs.execute()
    self.assertEqual(vs.execute(), 0x3C7876D8)
    
if __name__ == '__main__':
    unittest.main()
