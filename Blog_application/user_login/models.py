from django.db import models

# Create your models here.


class contact_model(models.Model):
    name_of_sender = models.CharField(max_length=20)
    email_of_sender = models.EmailField()
    message_of_sender = models.TextField(max_length=200)


class registered_users(models.Model):
    user_first_name = models.CharField(max_length=30)
    user_last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    user_phone = models.IntegerField()
    security_question = models.CharField(max_length=30)
    answer = models.CharField(max_length=20)
    user_password = models.CharField(max_length=13)
