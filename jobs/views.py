from django.shortcuts import render
from .models import Job, Publication

def job_list(request):
	jobs = Job.objects.all().order_by('end_date').reverse()
	publications = Publication.objects.all().order_by('publish_date').reverse()
	return render(request, 'jobs/job_list.html', {
		'jobs': jobs, 
		'publications': publications
		})