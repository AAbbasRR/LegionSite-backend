from django.db import models
from django.utils import timezone
from django.core import validators


class Comments(models.Model):
    class Meta:
        verbose_name = "نظر بازی"
        verbose_name_plural = "نظرات بازی ها"

    game = models.CharField(
        max_length=50,
        verbose_name='بازی'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='نام'
    )
    opinion = models.TextField(
        verbose_name='نظر'
    )
    rate = models.FloatField(
        default=2.5,
        validators=[validators.MinValueValidator(0.1), validators.MaxValueValidator(5.0)],
        verbose_name='رتبه'
    )
    accepted = models.BooleanField(
        default=False,
        verbose_name='وضعیت تایید شدن'
    )
    created_date = models.DateTimeField(
        default=timezone.now,
        verbose_name='تاریخ و زمان'
    )

    def __str__(self):
        return f'{self.game} - {self.name} - {self.created_date}'
