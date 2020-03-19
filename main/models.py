from django.db import models


class Todo(models.Model):
    text = models.CharField(max_length=255)
    time_added = models.DateTimeField()

    def __str__(self):
        return self.text
