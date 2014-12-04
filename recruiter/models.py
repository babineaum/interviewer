from django.db import models
from django import forms

class Recruiter(models.Model):

	recruiter_name = models.CharField(
		max_length=255,
	)

	recruiter_company = models.CharField(
		max_length=255,
	)

	recruiter_email = models.EmailField()

	recruiter_phone = forms.RegexField(regex=r'\d{9,15}$', error_message = ("Phone number must be entered in the format: '9999999999'. Up to 10 digits allowed."))

	recruiter_companies = models.CharField(
		max_length=255,
	)

	recruiter_notes = models.TextField()

	recruiter_contact_date = models.DateField(auto_now_add=True)

	recruiter_contact_date_latest = models.DateField(auto_now=True)

	recruiter_follow_up = models.CommaSeparatedIntegerField(max_length=512)

	def __unicode__(self):
		return '%s:%s' %(self.recruiter_name, self.recruiter_company)

class Company(models.Model):

	company_name = models.CharField(
		max_length=255,
	)

	hiring_manager = models.CharField(
		max_length=255,
	)

	hiring_mngr_email = models.EmailField()

	hiring_mngr_phone = forms.RegexField(regex=r'\d{9,15}$', error_message = ("Phone number must be entered in the format: '9999999999'. Up to 10 digits allowed."))

	company_notes = models.TextField()

	company_contact_date = models.DateField(auto_now_add=True)

	company_contact_date_latest = models.DateField(auto_now=True)

	company_follow_up = models.CommaSeparatedIntegerField(max_length=512)

	def __unicode__(self):
		return '%s:%s' %(self.company_name, self.hiring_manager)
