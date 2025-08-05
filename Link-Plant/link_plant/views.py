from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Profile, Link

# Create your views here.

# Class-based views
class LinkListView(ListView):
    model = Link
    # template called model_list.html -> link_list.html
    
class LinkCreateView(CreateView):
    model = Link
    fields = "__all__"
    # template called model_form -> link_form.html
    success_url = reverse_lazy('link-list')
    
    
class LinkUpdateView(UpdateView):
    model = Link
    fields = ["text", "url"]
    success_url = reverse_lazy('link-list')
    # template called model_form -> link_form.html
    
class LinkDeleteView(DeleteView):
    model = Link
    success_url = reverse_lazy('link-list')
    # form to submit to delete the item
    # expect a template name model_confirm_delete.html -> link_confirm_delete.html
    
def profile_view(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    links = profile.links.all()
    context = {
        "profile": profile,
        "links": links
    }
    
    return render(request=request, template_name="link_plant/profile.html", context=context)