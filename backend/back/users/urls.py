from django.urls import path
from .views import UserView
urlpatterns=[
    path('usuarios/', UserView.as_view(), name='user_list'),
]