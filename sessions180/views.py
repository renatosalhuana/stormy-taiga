from django.shortcuts import render, redirect
from .models import Day, Student
from .forms import StudentPresentationForm


# Create your views here.
def home(request):
    days = Day.objects.filter(published=True).order_by("date")
    return render(request, "sessions180/home.html", {"days": days})


def drafts(request):
    if request.user and request.user.is_staff:
        days = Day.objects.all().order_by("date")
        return render(request, "sessions180/drafts.html", {"days": days})
    return redirect("/")


def day_detail(request, slug):
    day = Day.objects.get(slug=slug)
    return render(request, "sessions180/day.html", {"day": day})
