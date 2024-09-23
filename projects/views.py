from django.shortcuts import render
from projects.models import Project
from personal_profile.models import Profile

# Create your views here.
def project_index(request):
    profile = Profile.objects.get(pk=1)
    projects = Project.objects.all()
    context = {
        'profile': profile,
        'projects': projects
    }
    return render(request, 'projects/project_index.html', context)

def project_detail(request,pk):
    profile = Profile.objects.get(pk=1)
    project = Project.objects.get(pk=pk)
    projects = Project.objects.all()
    context = {
        'profile': profile,
        'project': project,
        'projects': projects
    }
    return render(request, 'projects/project_detail.html', context)