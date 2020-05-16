from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Greeting
from sessions180.models import Student
from sessions180.forms import StudentPresentationForm


# Create your views here.
def index(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            new_user = form.save()
            student = Student()
            student.user_id = new_user.pk
            student.save()
            #student_form = StudentPresentationForm(response.POST, instance=student)
            return redirect("/sessions180")
            #return render(response, "sessions180/student_details.html", {"student_form": student_form})
    else:
        form = RegisterForm()

    return render(response, "index.html", {"form": form})


def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
