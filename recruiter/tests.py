from django.test import TestCase
from recruiter.models import Recruiter

class RecruiterTests(TestCase):
	def test_str(self):
		recruiter = Recruiter(recruiter_name="Al Jorgenson", recruiter_company="ACME Recruiters")

		self.assertEquals(
			str(recruiter),
			'Al Jorgenson:ACME Recruiters')
