from django.db import models

# Create your models here.


class User(models.Model):
    # 공백의 필요성 여부를 null = false를 통해서 알려준다
    user_email = models.CharField(max_length=30)
    user_pw = models.CharField(max_length=20)

class Note(models.Model):

    user_name = models.CharField(max_length=45)
    description = models.CharField(max_length=200)

class PostIt(models.Model):

    anonymous = models.BooleanField
    writer = models.CharField(max_length=20)
    content_text = models.TextField