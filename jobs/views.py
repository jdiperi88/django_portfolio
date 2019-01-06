from django.shortcuts import render

# import job model
from .models import Job
# Create your views here.


def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.htm', {'jobs': jobs})
