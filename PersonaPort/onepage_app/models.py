from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile/')
    footer_text = models.CharField(max_length=200, default='© 2025')

    def __str__(self):
        return self.name

class SocialLink(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='social_links')
    name = models.CharField(max_length=50)
    url = models.URLField()
    icon_style = models.CharField(max_length=10)
    icon_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} for {self.profile.name}'

class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.title
    
class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='educations')
    content = models.TextField()
    
class CV(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='cvs')
    cv_file = models.FileField(upload_to='documents/')