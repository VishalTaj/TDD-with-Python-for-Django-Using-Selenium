from django.test import TestCase

# Create your tests here.
class SimpleTest(TestCase):
    def test_basic_addition(self):
        self.assertEquals(1+1,3)
