from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Message
import json

# ------------------- Inbox View -------------------
@login_required
def chat_inbox(request):
    # Get all user IDs you’ve chatted with (sent or received)
    sent_to = Message.objects.filter(sender=request.user).values_list('receiver', flat=True)
    received_from = Message.objects.filter(receiver=request.user).values_list('sender', flat=True)

    # Combine all IDs and remove your own ID
    user_ids = set(sent_to) | set(received_from)
    user_ids.discard(request.user.id)

    # Get actual User objects
    users = User.objects.filter(id__in=user_ids)

    return render(request, 'chat/inbox.html', {'users': users})


# ------------------- Chat Page View -------------------
@login_required
def chat_with_user(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    
    # Get all messages between current user and other user
    messages = Message.objects.filter(
        sender__in=[request.user, other_user],
        receiver__in=[request.user, other_user]
    ).order_by('timestamp')
    
    return render(request, 'chat/chat.html', {
        'other_user': other_user,
        'messages': messages
    })


# ------------------- Send Message AJAX -------------------
@csrf_exempt
@login_required
def send_message_ajax(request, user_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = data.get('message')
            recipient = User.objects.get(id=user_id)

            msg = Message.objects.create(
                sender=request.user,
                receiver=recipient,
                content=message
            )

            return JsonResponse({
                'message': msg.content,
                'sender': request.user.username
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


# ------------------- Get Messages AJAX -------------------
@login_required
def get_messages_ajax(request, user_id):
    recipient = get_object_or_404(User, id=user_id)

    # Fetch messages between current user and recipient
    messages = Message.objects.filter(
        sender__in=[request.user, recipient],
        receiver__in=[request.user, recipient]
    ).order_by('timestamp')

    # Format for JSON
    messages_data = [
        {
            'sender': msg.sender.username,
            'message': msg.content,
            'timestamp': msg.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        }
        for msg in messages
    ]

    return JsonResponse({'messages': messages_data})
