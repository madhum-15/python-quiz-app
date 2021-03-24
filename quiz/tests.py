from django.test import TestCase
from django.test import tag
import unittest
class SampleTest(unittest.TestCase):
   # return True or False
   def test(self):
      self.assertTrue(True)
# running the test
unittest.main()
class SampleTestCase(TestCase):

    @tag('fast')
    def test_fast(self):
        ...

    @tag('slow')
    def test_slow(self):
        ...

    @tag('slow', 'core')
    def test_slow_but_core(self):
        ...
class MyTests(TestCase):
    @skipIfDBFeature('supports_transactions')
    def test_transaction_behavior(self):
        # ... conditional test code
        pass
