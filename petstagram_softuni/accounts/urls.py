from django.urls import path, include

from petstagram_softuni.accounts.views import login_user, register_user, details_user, delete_user, edit_user

urlpatterns = (
    path('login/', login_user, name='login user'),
    path('register/', register_user, name='register user'),
    path('profile/<int:pk>/', include([
        path('', details_user, name='details user'),
        path('edit/', edit_user, name='edit user'),
        path('delete/', delete_user, name='deletes user'),
    ])),
)

'''
Check if above works:
http://127.0.0.1:8000/accounts/login/
http://127.0.0.1:8000/accounts/register/
http://127.0.0.1:8000/accounts/profile/1/
http://127.0.0.1:8000/accounts/profile/1/edit/
http://127.0.0.1:8000/accounts/profile/1/delete/
'''