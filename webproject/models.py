from django.db import models

# Create your models here.


class Users(models.Model):
    # 공백의 필요성 여부를 null = false를 통해서 알려준다
    user_id = models.AutoField(primary_key=True)
    user_email = models.CharField(max_length=30)
    user_pw = models.CharField(max_length=20)

    class Meta:
        db_table = 'users'
class Note(models.Model):

    note_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=45)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'note'
class PostIt(models.Model):

    postit_id = models.AutoField(primary_key=True)
    note = models.ForeignKey('Note', on_delete=models.CASCADE)
    anonymous = models.BooleanField
    writer = models.CharField(max_length=20)
    content_text = models.TextField

    def __str__(self):
        return self.writer

    class Meta:
        db_table = 'postit'
