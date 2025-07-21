from django.urls import path
from . import views

urlpatterns = [
    path('chat/<int:user_id>/', views.chat_with_user, name='chat_with_user'),
]
