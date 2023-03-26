# from django.shortcuts import render, redirect
# from .models import Room, Message
# from django.http import HttpResponse, JsonResponse
# import requests
# import json

# # Create your views here.
# def home(request):
#     return render(request, 'login.html')

# def room(request, room):
#     username = request.GET.get('username')
#     room_details = Room.objects.get(name=room)
#     return render(request, 'room.html', {
#         'username': username,
#         'room': room,
#         'room_details': room_details
#     })

# def checkview(request):
    
#     room = request.POST.get('room_name', '')

#     username = request.POST['username']
#     if Room.objects.filter(name=room).exists():
#         return redirect('/'+room+'/?username='+username)
#     else:
#         new_room = Room.objects.create(name=room)
#         new_room.save()
#         return redirect('/'+room+'/?username='+username)



# def getMessages(request, room):
#     room_details = Room.objects.get(name=room)

#     messages = Message.objects.filter(room=room_details.id)
#     return JsonResponse({"messages":list(messages.values())})

# def shrinkbot(id_room):

#     url = "https://api.writesonic.com/v2/business/content/chatsonic?engine=premium"
#     print()
#     msg=Message.objects.all().last()
#     payload = {
#         "enable_google_results": "true",
#         "enable_memory": True,
#         "input_text": msg.value,
#         "history_data": [
#             {
#                 "is_sent": True,
#                 "message": "Respond every query like a professional therapist and separate the answer in points"
#             },
#         ]
#     }

#     # print(payload["history_data"])


#     headers = {
#         "accept": "application/json",
#         "content-type": "application/json",
#         "X-API-KEY": "d0dba82e-7f3a-4a4c-9e7d-cbe9dcbba1b9"
#     }
                        
#     response = requests.post(url, json=payload, headers=headers)
#     parsed_json = (json.loads(response.text))
#     bot_response=parsed_json
#     print(bot_response)
#     new_message = Message.objects.create(value=bot_response, user="BOT", room=id_room)
#     new_message.save()

#     # payload["history_data"]+=[{
#     #             "is_sent": True,
#     #             "message": payload["input_text"]
#     #         }]

#     # print(payload["history_data"])

# def send(request):
#     message = request.POST['message']
#     username = request.POST['username']
#     room_id = request.POST['room_id']

#     new_message = Message.objects.create(value=message, user=username, room=room_id)
#     new_message.save()
#     shrinkbot(room_id)

#     return HttpResponse('Message sent successfully')

# # def shrinkbot_response(request,response):


from django.shortcuts import render, redirect
from .models import Room, Message
from django.contrib.auth.models import auth,User
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
import requests
import json
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    print(room_details)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

def shrinkbot(id_room):

    url = "https://api.writesonic.com/v2/business/content/chatsonic?engine=premium"
    print()
    msg=Message.objects.all().last()
    payload = {
        "enable_google_results": "true",
        "enable_memory": True,
        "input_text": msg.value,
        "history_data": [
            {
                "is_sent": True,
                "message": "Respond every query like a professional therapist and separate the answer in points"
            },
        ]
    }

    # print(payload["history_data"])


    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "X-API-KEY": "d0dba82e-7f3a-4a4c-9e7d-cbe9dcbba1b9"
    }
                        
    response = requests.post(url, json=payload, headers=headers)
    parsed_json = (json.loads(response.text))
    bot_response=parsed_json
    print(bot_response)
    new_message = Message.objects.create(value=bot_response, user="BOT", room=id_room)
    new_message.save()

    # payload["history_data"]+=[{
    #             "is_sent": True,
    #             "message": payload["input_text"]
    #         }]

    # print(payload["history_data"])

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    print(username)
    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    shrinkbot(room_id)

    return HttpResponse('Message sent successfully')