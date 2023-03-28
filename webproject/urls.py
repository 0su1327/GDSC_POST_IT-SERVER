from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from webproject import views

app_name = "user"

urlpatterns= [

    path('', views.home, name='home'),
    path('login', views.ListUser.as_view(), name='login'),
    # path('logout', views.logout, name='logout'),
    # path('signup', views.signup, name='signup'),
    # path('note/<int:user_id>', views.create_note, name='create_note'),
    # path('note/<int:user_id>/check', views.note_check, name='note'),
    # path('note/<int:user_id>/write', views.create_postit, name='create_postit')
]

urlpatterns= format_suffix_patterns(urlpatterns)