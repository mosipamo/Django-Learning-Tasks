from django.shortcuts import render
from .models import Profile, SocialLink, Project

# Create your views here.
def index(request):
    profile = Profile.objects.first()
    
    context = {
        'profile': profile,
        'social_links': profile.social_links.all(),
        'projects': profile.projects.all(),
        'educations': profile.educations.all(),
        'cvs': profile.cvs.first()
    }
    return render(request, 'onepage_app/index.html', context)