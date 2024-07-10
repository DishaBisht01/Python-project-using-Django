from django.shortcuts import render, redirect
from .forms import CVForm

def home(request):
    if request.method == "POST":
        form = CVForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = CVForm()
    return render(request, 'home.html', {'form': form})

def success(request):
    return render(request, 'success.html')
