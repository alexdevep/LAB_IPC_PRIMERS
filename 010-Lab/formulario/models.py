from django.db import models
from django.conf import settings

# Create your models here.
class Formula(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.title