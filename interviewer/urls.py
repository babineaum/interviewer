from django.conf.urls import patterns, include, url
from django.contrib import admin
import recruiter.views

urlpatterns = patterns('',
	# Examples:
    # url(r'^$', 'interviewer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', recruiter.views.ListRecruiterView.as_view(),
    	name="recruiter_list",),
)
