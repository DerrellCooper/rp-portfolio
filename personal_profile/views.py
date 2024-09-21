from django.shortcuts import render
from projects.models import Project
# Create your views here.

def profile(request):
    #profile = profile.objects.get(pk=1)
    projects = Project.objects.all()
    context = {
        #'profile':profile,
        'projects': projects
    }
    return render(request, 'personal_profile/profile_main.html', context)