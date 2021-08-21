from django.shortcuts import render
from django.http import HttpResponse
from .models import Phone
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    user_no = User.objects.get(id = 1).phone
    print(user_no)

    user = Phone.objects.get(id=1).user_id
    print(user)






