from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('users/edit', views.edit_user, name='edit_user'),
    path('users/edit_done', views.edit_user_done, name='edit_user_done'),
]