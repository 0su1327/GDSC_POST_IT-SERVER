from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from webproject.models import *

from django.shortcuts import render, redirect
# from django.contrib.auth.models import Users
from django.contrib import auth


# Create your views here.

# 회원 가입
@csrf_exempt
def signup(request):
    # 새로운 유저를 만드는 절차
    if request.method == 'POST':
        data = Users.objects.all()
        context = {'data': data}

        # password와 confirm에 입력된 값이 같으면
        if request.POST['user_pw'] == request.POST['confirm']:
            # user 객체를 새로 생성
            try:

                user = Users(user_email = request.POST['user_email'], user_pw = request.POST['user_pw'])
                user.save()
            except :
                user = None
                return render(request, 'home.html', context)
    # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
    return render(request, 'signup.html')


# 로그인
# def login(request):
#     # login으로 POST 요청이 들어왔을 때, 로그인 절차를 밟는다.
#     if request.method == 'POST':
#         # login.html에서 넘어온 username과 password를 각 변수에 저장한다.
#         user_email = request.POST['user_email']
#         user_pw = request.POST['user_pw']
#
#         # 이건 auth를 사용할때만
#         # 해당 username과 password와 일치하는 user 객체를 가져온다.
#         # user = auth.authenticate(request, user_email=username, password=password)
#         #
#         # # 해당 user 객체가 존재한다면
#         # if user is not None:
#         # auth.login(request, user)
#         # 홈 화면으로
#         user = User()
#         user.user_email = request.POST['user_email']
#         user.user_pw = request.POST['user_email']
#
#             return render('home.html')
#         # 존재하지 않는다면
#         else:
#             # 딕셔너리에 에러메세지를 전달하고 다시 login.html 화면으로 돌아간다.
#             return render(request, 'login.html', {'error': 'username or password is incorrect.'})
#     # login으로 GET 요청이 들어왔을때, 로그인 화면을 띄워준다.
#     else:
#         return render(request, 'login.html')
#
#
# # 로그 아웃
# def logout(request):
#     # logout으로 POST 요청이 들어왔을 때, 로그아웃 절차를 밟는다.
#     if request.method == 'POST':
#         auth.logout(request)
#         return render(request, 'home.html')
#
#     # logout으로 GET 요청이 들어왔을 때, 로그인 화면을 띄워준다.
#     return render(request, 'login.html')
#
# def home(request):
#     return render(request, 'home.html')