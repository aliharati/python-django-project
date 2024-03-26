from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    my_dict = {'insert_here': "this is the inserted sentence from first app"}
    return render(request, "polls/index.html",context=my_dict)
