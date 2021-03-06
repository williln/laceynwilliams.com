from django.shortcuts import render
from .models import Job, Publication, Talk, Education

def job_list(request):
	jobs = Job.objects.all().order_by('end_date').reverse()
	publications = Publication.objects.all().order_by('publish_date').reverse()
	talks = Talk.objects.all().order_by('talk_date').reverse()
	schools = Education.objects.all().order_by('grad_date').reverse()
	return render(request, 'jobs/job_list.html', {
		'jobs': jobs, 
		'publications': publications, 
		'talks': talks,
		'schools': schools,
		})