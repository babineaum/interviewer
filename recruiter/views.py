from django.views.generic import ListView
from recruiter.models import Recruiter

class ListRecruiterView(ListView):
	model = Recruiter
	template_name = 'recruiter_list.html'