from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Greeting


# Create your views here.
def index(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/sessions180")
    else:
        form = RegisterForm()

    return render(response, "index.html", {"form": form})


def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
