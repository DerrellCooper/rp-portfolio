from django.shortcuts import render

# Create your views here.

def profile(request):
    # profile = profile.objects.get(pk=1)
    # context = {
    #     'profile':profile
    # }
    return render(request, 'personal_profile/profile_main.html')