from django.shortcuts import render, get_object_or_404
from .models import JobPosting

# Create your views here.
def index(request):
    active_postings = JobPosting.objects.filter(is_active=True)
    context = {
        "job_postings": active_postings
    }
    return render(request, "job_board/index.html", context)

def job_detail(request, pk):
    # job = JobPosting.objects.get(pk=pk)
    job = get_object_or_404(JobPosting, pk=pk, is_active=True)
    context = {
        "job_postings": job
    }
    return render(request, "job_board/detail.html", context)