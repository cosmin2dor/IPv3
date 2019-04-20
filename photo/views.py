from django.shortcuts import render, redirect
from .models import PhotoModel
from .forms import PhotoForm
from users.models import CustomUser


def home_view(request):
    if not request.user.is_authenticated:
        return redirect('/users/login/')

    wall = PhotoModel.objects.all().order_by('-timestamp')
    liked_photos = []
    for photo in wall:
        if photo.likes.filter(pk=request.user.id).exists():
            liked_photos.append(photo.id)

    print(liked_photos)

    return render(request, "home.html", {'wall': wall, 'likesTo': liked_photos})


def upload_view(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            new_photo = PhotoModel()
            new_photo.description = form.cleaned_data['description']
            new_photo.image_url = form.cleaned_data['image_url']
            new_photo.keywords = form.cleaned_data['keywords']
            custom_user = CustomUser.objects.get(username=request.user.username)
            new_photo.user = custom_user
            new_photo.save()
            return redirect('home')

    else:
        form = PhotoForm()
    return render(request, "upload.html", {'form': form})


def like_action(request, pk):
    user = CustomUser.objects.get(id=request.user.id)

    likes_field = PhotoModel.objects.get(pk=pk).likes

    if likes_field.filter(pk=user.pk).exists():
        likes_field.remove(user)
    else:
        likes_field.add(user)

    return redirect('home')
