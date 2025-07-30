from django.shortcuts import render, get_object_or_404, redirect
from .models import Link
from .forms import LinkForm
from django.urls import reverse

# Create your views here.
def index(request):
    links = Link.objects.all()
    context = {
        "links": links
    }
    
    return render(request=request, template_name='links/index.html', context=context)


def root_link(request, link_slug):
    link = get_object_or_404(Link, slug=link_slug)
    link.click()
    
    return redirect(to=link.url)

def add_link(request):
    if request.method == "POST":
        form = LinkForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect(to=reverse("home"))
    else:
        form = LinkForm()
    
    context = {
        "form": form
    }
    return render(request=request, template_name='links/create.html', context=context)