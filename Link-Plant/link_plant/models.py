from django.db import models

# Create your models here.
# Profiles -> Links 

class Profile(models.Model):
    # name, slug, bg-color
    BG_CHOICES = (
        ('white', 'White'),
        ('black', 'Black'),
        ('red', 'Red'),
        ('green', 'Green'),
        ('blue', 'Blue'),
        ('yellow', 'Yellow'),
    )
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    bg_color = models.CharField(max_length=7, choices=BG_CHOICES, default='#FFFFFF')
    
    def __str__(self):
        return self.name
    
# many to one model
class Link(models.Model):
    # text, url, profile
    text = models.CharField(max_length=100)
    url = models.URLField(max_length=100)
    profile = models.ForeignKey(Profile, related_name='links', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.text} | {self.url}"