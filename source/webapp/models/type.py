from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=50, verbose_name='Тип')

    def __str__(self):
        return self.name

