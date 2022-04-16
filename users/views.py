from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}.")
            return redirect('login')
    else:
        form = UserRegisterForm()
    form.fields['username'].widget.attrs.update({
            'placeholder': 'Username'
        })
    form.fields['email'].widget.attrs.update({
            'placeholder': 'Email'
        })
    form.fields['password1'].widget.attrs.update({
            'placeholder': 'Password'
        })
    form.fields['password2'].widget.attrs.update({
            'placeholder': 'Re-Enter Password'
        })

    return render(request, 'register.html', {'form':form})

@login_required
def favorites(request):
    return render(request, 'favorites.html')