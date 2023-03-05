from django.http import HttpResponse
from django.shortcuts import render

from webproject.models import User


# Create your views here.

# 회원가입
def signup(request) :
        if request.method == "GET":
            return render(request, 'base.html')
        elif request.method == "POST":
            user_email = request.POST['user_email']
            user_pw = request.POST

            user = User(
                user_email = user_email,
                user_pw = user_pw,
            )

            User.save()

            return render(request, 'new_base.html')

# def login(request) :
#     if request.method == "GET":
#         return render(request, 'base.html')
#     elif request.method == "POST":
#         user