from django.urls import path
from . import views

urlpatterns = [
    path('chat/<int:user_id>/', views.chat_with_user, name='chat_with_user'),
    path('inbox/', views.chat_inbox, name='chat_inbox'),
    
    path('send_message_ajax/<int:user_id>/', views.send_message_ajax, name='send_message_ajax'),
    path('get_messages_ajax/<int:user_id>/', views.get_messages_ajax, name='get_messages_ajax'),
]

