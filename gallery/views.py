from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.decorators import login_required
from .forms import ArtworkForm


# Create your views here.
def home(request):
    return render(request, 'gallery/home.html')


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Your account was created successfully.")
            return redirect("home")
    else:
        form = RegistrationForm()

    return render(request, "gallery/register.html", {"form": form})


@login_required
def upload_artwork(request):
    if request.method == "POST":
        form = ArtworkForm(request.POST, request.FILES)

        if form.is_valid():
            artwork = form.save(commit=False)
            artwork.artist = request.user
            artwork.save()
            messages.success(request, "Your artwork was uploaded successfully!")
            return redirect("home")
    else:
        form = ArtworkForm()

    return render(request, "gallery/upload.html", {"form": form})
