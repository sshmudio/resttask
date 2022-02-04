from django.db import models
from django.utils import timezone
import datetime


class Users(models.Model):

    id = models.AutoField(verbose_name='id', primary_key=True)
    username = models.CharField(verbose_name='username', max_length=150)
    email = models.EmailField(verbose_name='email')
    password = models.CharField(verbose_name='password', max_length=255)
    register_date = models.DateTimeField(verbose_name='register_date', default=timezone.now)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now
