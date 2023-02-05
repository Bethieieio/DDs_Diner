from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class BookingModel(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bookings',
    )
    date = models.DateField()
    time = models.TimeField()
    heads = models.IntegerField()
    allergies = models.BooleanField(default=False)


class PreorderModel(models.Model):
    head_name = models.TextField()
    main = models.TextField()
    side = models.TextField()
    dessert = models.TextField()
    drink = models.TextField()
    booking = models.ForeignKey(
        BookingModel,
        on_delete=models.CASCADE,
        related_name='preorders',
    )


class CreateReviews(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    review = models.TextField()
    creation_date = models.DateTimeField(default=now)


class LikeReviews(models.Model):
    like_unlike = models.BooleanField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='like_unlike',
    )
    review = models.ForeignKey(
        CreateReviews,
        on_delete=models.CASCADE,
        related_name='like_unlike',
    )
