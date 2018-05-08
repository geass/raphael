from django.db import models
from django.contrib.auth.models import User

class Restaurants(models.Model):
    slug = models.SlugField(db_index=True, max_length=255, unique=True)
    title = models.CharField(db_index=True, max_length=255)
    description = models.TextField()
    body = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'restaurants'

    def __str__(self):
        return self.title