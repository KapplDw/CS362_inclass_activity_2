import unittest
import wordCount

class wordCountTestCase(unittest.TestCase):
    def test_count(self):
        self.assertEqual(wordCount.lengthSent("This is an activity"), 4)
        self.assertEqual(wordCount.lengthSent("Testing a longer senctence than four words long."), 8)
        self.assertEqual(wordCount.lengthSent("Fail case"), 1) # Fail case