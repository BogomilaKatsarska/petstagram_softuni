from django.urls import path

from petstagram_softuni.common.views import index, like_photo

urlpatterns = (
    path('', index, name='index'),
    path('like/<int:photo_id>/', like_photo, name='like photo'),
)

'''
Check if above works:
http://127.0.0.1:8000/
'''