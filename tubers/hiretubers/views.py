from django.shortcuts import render
from .models import Hiretuber
from django.contrib import messages
# Create your views here.


def hiretuber(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        tuber_id = request.POST['tuber_id']
        tuber_name = request.POST['tuber_name']
        message = request.POST['message']
        city = request.POST['city']
        state = request.POST['state']
        phone = request.POST['phone']
        email = request.POST['email']
        user_id = request.POST['user_id']

        # TODO: 'Make all the neccessary checking and authorization needed'

        hiretuber = Hiretuber(first_name=first_name, last_name=last_name, tuber_id=tuber_id, tuber_name=tuber_name, message=message, city=city, state=state, phone=phone, email=email, user_id=user_id)
        hiretuber.save()
        messages.success(request, 'Thanks for reaching out!')
        return redirect('youtubers')