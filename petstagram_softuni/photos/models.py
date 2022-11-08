from django.db import models


class Photo(models.Model):
    MIN_DESCRIPTION_LEN = 10
    MAX_DESCRIPTION_LEN = 300
    MAX_LOCATION_LEN = 30
    photo = models.ImageField(
        null=False,
        blank=True,
    )
    description = models.CharField(

    )
    location = models.CharField()
    publication_date = models.DateField(

    )
