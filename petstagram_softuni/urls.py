from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('petstagram_softuni.common.urls')),
    path('photos/', include('petstagram_softuni.photos.urls')),
    path('accounts/', include('petstagram_softuni.accounts.urls')),
    path('pets/', include('petstagram_softuni.pets.urls')),
]
