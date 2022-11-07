from django.urls import path

from petstagram_softuni.common.views import index

urlpatterns = (
    path('', index, name='index'),
)

'''
Check if above works:
http://127.0.0.1:8000/
'''