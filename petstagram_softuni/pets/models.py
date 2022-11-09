from django.db import models
from django.utils.text import slugify
from petstagram_softuni.core.model_mixins import StrFromFieldsMixin


class Pet(StrFromFieldsMixin, models.Model):
    str_fields = ('id', 'name', 'slug')
    MAX_NAME = 30
    name = models.CharField(
        max_length=MAX_NAME,
        null=False,
        blank=False,
    )
    personal_photo = models.URLField(
        null=False,
        blank=False,
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    def save(self, *args, **kwargs):
        # create/update
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.name}')
        # update
        return super().save(*args, **kwargs)


    # def __str__(self):
    #     return f'ID: {self.id} | Name: {self.name}'