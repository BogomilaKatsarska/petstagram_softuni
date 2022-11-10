from petstagram_softuni.common.models import PhotoLike


def get_user_liked_photo(photo_id):
    return PhotoLike.objects.filter(photo_id=photo_id)


def get_photo_url(request, photo_id):
    return request.META['HTTP_REFERER'] + f'#photo-{photo_id}'
