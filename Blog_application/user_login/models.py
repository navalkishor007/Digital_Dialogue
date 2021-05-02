from django.db import models

# Create your models here.


class contact_model(models.Model):
    name_of_sender = models.CharField(max_length=20)
    email_of_sender = models.EmailField()
    message_of_sender = models.TextField(max_length=200)
