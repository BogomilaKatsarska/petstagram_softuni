from django.contrib import admin

from petstagram_softuni.common.models import PhotoComment


@admin.register(PhotoComment)
class PhotoCommentAdmin(admin.ModelAdmin):
    pass