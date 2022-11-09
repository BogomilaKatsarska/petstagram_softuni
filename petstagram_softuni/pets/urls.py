from django.urls import path, include

from petstagram_softuni.pets.views import add_pet, details_pet, edit_pet, delete_pet

urlpatterns = (
    path('add/', add_pet, name='add pet'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', details_pet, name='details pet'),
        path('edit/', edit_pet, name='edit pet'),
        path('delete/', delete_pet, name='delete pet'),
         ])),
)

'''
Check if above works:
http://127.0.0.1:8000/pets/add/
http://127.0.0.1:8000/pets/bogomila/pet/thumper/
http://127.0.0.1:8000/pets/bogomila/pet/thumper/edit/
http://127.0.0.1:8000/pets/bogomila/pet/thumper/delete/
'''