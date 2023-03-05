from django.urls import path

from webproject.views import hello_world

app_name = "accountapp"

urlpatterns= [
    path('/login', hello_world, name='hello_world')
]