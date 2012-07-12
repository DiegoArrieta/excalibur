"""
This File demonstrates writing tets using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropiate tests for your applicaction.
"""

from django.test import TestCase

class SimpleTest(TestCase):
	def test_basic_addition(self):
		"""
		Tests that 1 + 1 always equals 2.
		"""
		self.assertEqual(1+1,2)
