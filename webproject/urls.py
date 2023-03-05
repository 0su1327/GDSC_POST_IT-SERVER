from django.urls import path

from webproject import views


app_name = "accountapp"

urlpatterns= [
    # path('/login', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]