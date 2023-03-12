from django.urls import path

from webproject import views

app_name = "user"

urlpatterns= [

    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('note/:user_id/make', views.create_note, name='create_note'),
    path('note/:user_id', views.note_check, name='note'),
    path('note/:note_id/write', views.create_postit, name='create_postit')
]