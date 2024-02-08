from django.shortcuts import render
from chat.models import Chat
# Create your views here.


def chat(request):
    return render(request,'chat/Chat.html')