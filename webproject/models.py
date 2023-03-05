from django.db import models

# Create your models here.


class User(models.Model):
    # 공백의 필요성 여부를 null = false를 통해서 알려준다
    user_id = models.AutoField(primary_key=True)
    user_email = models.CharField(max_length=30)
    user_pw = models.CharField(max_length=20)

    class Meta:
        db_table = 'user'
        fields = ['']
class Note(models.Model):

    user_name = models.CharField(max_length=45)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name
class PostIt(models.Model):

    anonymous = models.BooleanField
    writer = models.CharField(max_length=20)
    content_text = models.TextField

    def __str__(self):
        return self.writer