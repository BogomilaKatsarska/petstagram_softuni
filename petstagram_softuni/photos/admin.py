from django.contrib import admin

from petstagram_softuni.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'publication_date', 'pets')

    @staticmethod
    def pets(current_photo_object):
        return ', '.join(p.name for p in current_photo_object.tagged_pets.all())

