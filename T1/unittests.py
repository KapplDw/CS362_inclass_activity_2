import unittest

import palindrone

class TestPalindrome(unittest.TestCase):
    
    def test_palind(self):
        self.assertEqual(palindrone.palind("Racecar"),True)
        self.assertEqual(palindrone.palind("car"),False)
        self.assertEqual(palindrone.palind("fail"), True) # Fail case to test that it does flag fails

if __name__ == '__main__':
    unittest.main()
