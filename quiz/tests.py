from django.test import TestCase
from django.test import tag
import unittest
class SampleTest(unittest.TestCase):
   # return True or False
   def test(self):
      self.assertTrue(True)
# running the test
if __name__ == '__main__':
    unittest.main()
