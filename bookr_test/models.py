from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=50, help_text="The name of the Publisher")
    website = models.URLField(help_text="The Publisher website")
    email = models.EmailField(help_text="The Publisher email address")
    def __str__(self):
        return self.name
    # Create your models here.
