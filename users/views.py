from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from users.models import CustomUser
from photo.models import PhotoModel
from django.http import JsonResponse

from .forms import CustomUserCreationForm


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, "registration/signup.html", {'form': form})


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': CustomUser.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'Username {} already exists.'.format(username)
    return JsonResponse(data)
