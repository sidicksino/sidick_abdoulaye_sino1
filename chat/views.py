from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import make_aware
from datetime import datetime

# View for home page
def home(request):
    return render(request, 'chat/home.html')

# View for chat room
def room(request, room):
    username = request.GET.get('username', 'Guest')  # Default to 'Guest' if no username
    try:
        room_details = Room.objects.get(name=room)  # Fetch the room from the database
    except Room.DoesNotExist:
        return HttpResponse("Room not found", status=404)

    return render(request, 'chat/room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

# View to handle room creation or entering an existing room
def checkview(request):
    if request.method == "POST":
        room_name = request.POST.get('room_name')
        username = request.POST.get('username')

        # Validate that both fields are provided
        if not room_name or not username:
            return HttpResponse("Room name or username not provided", status=400)

        # Check if the room exists; if not, create it
        room, created = Room.objects.get_or_create(name=room_name)

        # Redirect to the chat room
        return redirect(f'/chat/room/{room_name}/?username={username}')
    else:
        return redirect('chat:home')

# View to handle sending messages

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    
    # Create a naive datetime (if needed)
    naive_date = datetime.now()
    
    # Convert to timezone-aware datetime
    aware_date = make_aware(naive_date)

    # Save the message with the aware datetime
    new_message = Message.objects.create(value=message, user=username, room_id=room_id, date=aware_date)
    new_message.save()
    return HttpResponse('Message sent successfully')

# View to get messages in a room
def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})

# Index page for the chat application
def index(request):
    return render(request, 'chat/home.html')

def message_view(request):
    username = request.GET.get('username', 'Guest')  # Default to 'Guest' if no username
    return render(request, 'chat/message.html', {'username': username})


