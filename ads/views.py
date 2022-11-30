from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Ad
from .forms import AdForm
from django.utils import timezone
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def new(request):
    form = AdForm(request.POST or None)
    if request.method == "POST":
        form = AdForm(request.POST)
        ad = form.save(commit=False)
        ad.save()
        messages.success(request, 'Ваше объявление успешно отпавлено на модерацию.')
    form = AdForm()
    return render(request, 'form.html', {'form': form})