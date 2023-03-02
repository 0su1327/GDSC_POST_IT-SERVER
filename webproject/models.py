from django.db import models

# Create your models here.


class HelloWorld(models.Model):
    # 공백의 필요성 여부를 null = false를 통해서 알려준다
    text= models.CharField(max_length=255, null=False)