from django.contrib import admin
from .models import Profile, Project, SocialLink, Education, CV

# Register your models here.
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(SocialLink)
admin.site.register(Education)
admin.site.register(CV)