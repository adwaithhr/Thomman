from django.shortcuts import render, redirect
from .models import Chat, Queries
from django.contrib.auth.models import auth, User
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
import requests
import json
from django.contrib.auth.decorators import login_required


@login_required
def profile(request, username):
    name = User.objects.filter(username=username).first(
    ).first_name+" "+User.objects.filter(username=username).first().last_name
    if (Chat.objects.filter(user=username).exists()) == False:
        new_chat = Chat.objects.create(user=username, title='title')
        new_chat.save()
    chat = Chat.objects.filter(user=username).first()
    print(name)
    return render(request, 'profile.html', {
        'name': username,
        'chat': chat
    })


def chatroom(request, username):
    print("hi3"+username)

    send(request)
    # print("hi1")
    chat = Chat.objects.filter(user=username).first()
    name = User.objects.filter(username=username).first(
    ).first_name+" "+User.objects.filter(username=username).first().last_name
    print(chat.title)
    return render(request, 'chatroom.html', {
        'name': username,
        'chat': chat
    })


def getQueries(request, username):
    print("hi2")
    chat = Chat.objects.filter(user=username).first()
    messages = Queries.objects.filter(chat=chat.id)
    return JsonResponse({"messages": list(messages.values())})


def shrinkbot(id_chat):
    print("hi4")
    url = "https://api.writesonic.com/v2/business/content/chatsonic?engine=premium"
    print()
    qry = Queries.objects.all().last()
    payload = {
        "enable_google_results": "true",
        "enable_memory": True,
        "input_text": qry.value,
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
        "X-API-KEY": "714e2aa2-0c49-4af1-b671-8dfcae623239"
    }

    response = requests.post(url, json=payload, headers=headers)
    parsed_json = json.loads(response.text)
    bot_response = parsed_json
    print(bot_response)
    new_message = Queries.objects.create(
        value=bot_response['message'] if 'message' in bot_response else bot_response['detail'], name="BOT", chat=id_chat)
    new_message.save()

    # payload["history_data"]+=[{
    #             "is_sent": True,
    #             "message": payload["input_text"]
    #         }]

    # print(payload["history_data"])


def send(request):
    print("hi3")
    message = request.POST['message']
    username = request.POST['name']
    name = User.objects.filter(username=username).first(
    ).first_name+" "+User.objects.filter(username=username).first().last_name
    chat_id = request.POST['chat_id']
    print(f"........{chat_id}")
    print(name)
    new_message = Queries.objects.create(
        value=message, name=name, chat=chat_id)
    new_message.save()
    shrinkbot(chat_id)
    return HttpResponse('Message sent successfully')


def logout_view(request):
    print("hi5")
    auth.logout(request)
    return redirect("login")
