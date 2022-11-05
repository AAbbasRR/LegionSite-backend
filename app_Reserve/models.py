from django.db import models
from django.core import validators


class Sans(models.Model):
    class Meta:
        verbose_name = 'سانس'
        verbose_name_plural = 'سانس ها'

    start_hour = models.IntegerField(
        validators=[validators.MinValueValidator],
        verbose_name='ساعت شروع'
    )
    end_hour = models.IntegerField(
        validators=[],
        verbose_name='ساعت پایان'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        default=0,
        verbose_name="مبلغ"
    )
