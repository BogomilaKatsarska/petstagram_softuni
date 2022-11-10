from django.shortcuts import render, redirect
from django.urls import reverse
from petstagram_softuni.common.models import PhotoLike
from petstagram_softuni.common.utils import get_user_liked_photo, get_photo_url
from petstagram_softuni.core.photo_utils import apply_likes_count, apply_user_liked_photo
from petstagram_softuni.photos.models import Photo
import pyperclip


def index(request):
    photos = [apply_likes_count(photo) for photo in Photo.objects.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    context = {
        'photos': photos,
    }
    return render(request, 'common/home-page.html', context)


def like_photo(request, photo_id):
    user_liked_photos = get_user_liked_photo(photo_id)
    if user_liked_photos:
        user_liked_photos.delete()
    else:
    # OPTION 1:
        photo_like = PhotoLike(
            photo_id=photo_id,
        )
        photo_like.save()

    # OPTION 2:
    # PhotoLike.objects.create(
    #     photo_id=photo_id,
    # )

    return redirect(get_photo_url(request, photo_id))


def share_photo(request, photo_id):
    photo_details_url = reverse('details photo', kwargs={
        'pk': photo_id
    })
    pyperclip.copy(photo_details_url)
    return redirect(get_photo_url(request, photo_id))

