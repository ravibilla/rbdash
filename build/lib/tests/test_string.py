import unittest

from rbdash import RbDash

class Test(unittest.TestCase):
    def test_lower_method(self):
        self.assertEqual(RbDash.lower("TEST"), "test")
        self.assertNotEqual(RbDash.lower("test"), "TEST")

    def test_upper_method(self):
        self.assertEqual(RbDash.upper("test"), "TEST")
        self.assertNotEqual(RbDash.upper("TEST"), "test")

    def test_title_method(self):
        self.assertEqual(RbDash.title("hello world"), "Hello World")
        self.assertNotEqual(RbDash.title("hELLO wORLD"), "hello world")

    def test_kebab_method(self):
        self.assertEqual(RbDash.kebab("Kebab case adds hyphens BetWEEN lowerCASE text"),
                         "kebab-case-adds-hyphens-between-lowercase-text")
        self.assertNotEqual(RbDash.kebab("Kebab case doesn't contain spaces"), "kebab-case-doesn't contain spaces")
