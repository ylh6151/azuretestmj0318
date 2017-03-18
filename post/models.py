from django.db import models


class Postit(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    message = models.TextField(null=True)
    image = models.ImageField(null=True)
