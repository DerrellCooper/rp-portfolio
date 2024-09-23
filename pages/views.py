from django.shortcuts import render
from projects.models import Project
from personal_profile.models import Profile
# Create your views here.
def home(request):
    projects = Project.objects.all()
    profile = Profile.objects.get(pk=1)
    project = Project.objects.get(pk=1)

    context = {
        'projects': projects,
        'profile': profile,
        'project': project,

    }
    return render(request, 'pages/home.html', context)