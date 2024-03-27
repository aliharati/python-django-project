from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    my_dict = {'insert_here': "Here's an award winning painting made by AI:"}
    return render(request, "polls/index.html",context=my_dict)

def main(request):
    return render(request, 'index.html')