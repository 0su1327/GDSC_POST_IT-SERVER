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
        # data = Users.objects.all()
        # context = {'data': data}

        # password와 confirm에 입력된 값이 같으면
        if request.POST['user_pw'] == request.POST['confirm']:
            # user 객체를 새로 생성
            try:

                user = Users(user_email = request.POST['user_email'], user_pw = request.POST['user_pw'])
                user.save()
                return render(request, 'home.html', {'success': 'success'})
            except :
                user = None
                return render(request, 'home.html')
    # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
    return render(request, 'signup.html')


# 로그인
def login(request):
    # login으로 POST 요청이 들어왔을 때, 로그인 절차를 밟는다.
    if request.method == 'POST':

        # data = Users.objects.filter()
        # context = {'data': data}


        if Users.objects.filter(user_email= request.POST['user_email'], user_pw =request.POST['user_pw']).exists() == False:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})


        else:
            # home에서 context로 user_id를 받을 수 있다.
            data = Users.objects.filter(user_email=request.POST['user_email'])
            context = {'data': data}

            id = context.user_id

            if Note.objects.filter(user_id=id) :

               return render(request, 'note_check.html', {'note_exist': 'true'})
            return render(request, 'home.html', {'note_exist': 'false'})
    # login으로 GET 요청이 들어왔을때, 로그인 화면을 띄워준다.
    return render(request, 'create_note.html')


# # 로그 아웃
def logout(request):
    # logout으로 POST 요청이 들어왔을 때, 로그아웃 절차를 밟는다.
    return render(request, 'login.html')
#
def home(request):
    return render(request, 'home.html')


def create_note(request):
    if request.method == 'POST':

        note = Note(user_name=request.POST['user_name'], description=request.POST['description'])
        note.save()

        # 해당 user_name과 부합하는 데이터만 front에게 넘겨주어서 사용할 수 있도록 한다.
        data = Note.objects.filter(user_name=request.POST['user_name'])
        context = {'data': data}
        return render(request, 'note_check.html', context)


    else :
        
        # request.id 이런식으로 받아서 filter 거쳐서 쓰면 될듯
        # context
        data = Note.objects.all()
        context = {'data': data}
        return render(request, 'create_note.html', context)

def note_check(request):
    data = Postit.objects.all()
    context = {'data': data}
    return render(request, 'note_check.html', context)

def create_postit(request):
    if request.method == 'POST':

        # note_id 받으면 그걸 토대로 note_id에도 값을 넣어야함.
        postit = Postit(writer=request.POST['writer'], anonymous=request.POST['anonymous'], content_text = request.POST['content_text'])
        postit.save()


        # data = Note.objects.all()
        # context = {'data': data}
        # 성공하면 success를 주고 note_check.html로 rendering
        return render(request, 'note_check.html', {'success': 'success'})


    else :
        # context

        # 여기서도 note id 받으면 그걸 토대로 filter를 통해 user_name을 반환하기

        data = Note.objects.all()
        context = {'data': data}
        return render(request, 'create_postit.html', context)