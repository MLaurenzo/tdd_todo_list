from django.db import models


class Todo(models.Model):
    todo = models.CharField(max_length=200)
