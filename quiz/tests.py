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
import random
try:
    import unittest2 as unittest
except ImportError:
    import unittest

class SimpleTest(unittest.TestCase):
    @unittest.skip("demonstrating skipping")
    def test_skipped(self):
        self.fail("shouldn't happen")

    def test_pass(self):
        self.assertEqual(10, 7 + 3)

    def test_fail(self):
        self.assertEqual(11, 7 + 3)
