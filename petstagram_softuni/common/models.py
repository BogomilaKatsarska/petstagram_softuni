from django.db import models

from petstagram_softuni.photos.models import Photo


class PhotoComment(models.Model):
    MAX_COMMENT_LEN = 300
    comment = models.CharField(
        max_length=MAX_COMMENT_LEN,
        null=False,
        blank=False,
    )
    publication_date_and_time = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
    )
    photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )


class PhotoLike(models.Model):
    # field in relation is {NAME_OF_THIS_MODEL}_set
    # e.g.: Photo's field for likes is named photolike_set
    photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )
    # user = models.ForeignKey(
    #     User,
    # )
