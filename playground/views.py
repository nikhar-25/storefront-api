from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
#request handler
#action

# def cal(): # for debug
#     x = 1
#     y = 2
#     return x

def say_hello(request):
    #x = cal() # for debug
    return render(request, 'hello.html', {'name' : 'Nikhar'})
