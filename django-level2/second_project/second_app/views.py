from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import User
def index(request):
    return render(request,"index.html")

def user(request):
    user_list = User.objects.order_by("firstName")
    users = {'users': user_list }
    return render(request, "user/user.html", context=users)