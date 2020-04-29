from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.urls import reverse

from .forms import UserRegisterForm
from .models import Profile


def home(request):
    profiles = Profile.objects.all()
    context = {"profiles": profiles}
    return render(request, 'users/home.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("home"))
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
