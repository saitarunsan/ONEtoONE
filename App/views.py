from django.shortcuts import render
from django.http import HttpResponse
from .models import Phone
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    user_phone_no = User.objects.get(id = 1).phone#to get user phone no.
    print('phone no is:',user_phone_no)

    user = Phone.objects.get(id=1).user #this is reverse one to get user associated with phone no.
    print('name of user is:',user)


