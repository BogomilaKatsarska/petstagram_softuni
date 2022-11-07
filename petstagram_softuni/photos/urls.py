from django.urls import path, include

from petstagram_softuni.photos.views import add_photo, details_photo, edit_photo

urlpatterns = (
    path('add/', add_photo, name='add photo'),
    path('<int:pk>/', include([
        path('', details_photo, name='details photo'),
        path('edit/', edit_photo, name='edit photo'),
    ])),
)


'''
Check if above works:
http://127.0.0.1:8000/photos/add/
http://127.0.0.1:8000/photos/2/
http://127.0.0.1:8000/photos/1/edit/
'''