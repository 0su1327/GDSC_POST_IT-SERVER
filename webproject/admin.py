from django.contrib import admin
# #
# # # Register your models here.
from .models import Users
from .models import Note
from .models import Postit
# #같은 경로의 models.py에서 User라는 클래스를 임포트한다.
#
# # Register your models here.
#
# class UserAdmin(admin.ModelAdmin) :
#     list_display = ('username', 'password')
#
#
# admin.site.register(User, UserAdmin) #site에 등록

admin.site.register(Users)
admin.site.register(Note)
admin.site.register(Postit)