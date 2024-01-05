from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm

def SignUpPageView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = CustomUserCreationForm(request.POST)

    return render(request, 'registration/signup.html', {'form' : form})

