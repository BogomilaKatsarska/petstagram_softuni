from django.contrib import admin

from petstagram_softuni.pets.models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass
