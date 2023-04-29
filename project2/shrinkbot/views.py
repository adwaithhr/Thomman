from django.shortcuts import render, redirect
from .models import Chat, Queries
from django.contrib.auth.models import auth, User
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
import requests
import openai
import time
from django.contrib.auth.decorators import login_required

openai.api_key = "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"


@login_required
def profile(request, username):
    if (Chat.objects.filter(user=username).exists()) == False:
        new_chat = Chat.objects.create(user=username, title='title')
        new_chat.save()
    chat = Chat.objects.filter(user=username).first()
    return render(request, 'profile.html', {
        'name': username,
        'chat': chat
    })


def chatroom(request, username):
    send(request)
    chat = Chat.objects.filter(user=username).first()
    # print(chat.title)
    return render(request, 'chatroom.html', {
        'name': username,
        'chat': chat
    })


def getQueries(request, username):
    chat = Chat.objects.filter(user=username).first()
    messages = Queries.objects.filter(chat=chat.id)
    return JsonResponse({"messages": list(messages.values())})


def shrinkbot(id_chat):
    qry = Queries.objects.all().last()
    prompt = qry.value
    prompt = "Respond like a professional therapist to the user for the the issue\"" + \
        prompt+"\" Give answer in differnt lines"

    # Generate a response to the user's prompt
    response = generate_response(prompt)

    # Display the response to the user
    print(response)
    new_message = Queries.objects.create(
        value=response, name="MindMate", chat=id_chat)
    new_message.save()


def send(request):
    message = request.POST['message']
    username = request.POST['name']
    name = User.objects.filter(username=username).first().first_name+" " +\
        User.objects.filter(username=username).first().last_name
    chat_id = request.POST['chat_id']
    # print(f"........{chat_id}")
    # print(name)
    new_message = Queries.objects.create(
        value=message, name=name, chat=chat_id)
    new_message.save()
    shrinkbot(chat_id)
    return HttpResponse('Message sent successfully')


def logout_view(request):
    auth.logout(request)
    return redirect("login")


def generate_response(prompt):
    # Set up OpenAI API request parameters
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Extract the response text from the API response
    message = completions.choices[0].text.strip()

    return message
