from django.shortcuts import render
from .models import Day, Student
from .forms import StudentPresentationForm


# Create your views here.
def home(request):
    # student_name = ""
    # if response.method == "POST":
    #     form = StudentPresentationForm(response.POST)
    #     if form.is_valid():
    #         form.user_id = response.user.id
    #         form.save()
    #         student_name = form.cleaned_data['name']

    days = Day.objects.all().order_by("date")
    return render(request, "sessions180/home.html", {"days": days})


def day_detail(request, slug):
    day = Day.objects.get(slug=slug)
    return render(request, "sessions180/day.html", {"day": day})
