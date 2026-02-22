from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calculate(x, y):
    x= x + 5
    y= y + 10
    return x + y

def sayHello(request):
    x=10
    y=20
    calculate(x, y)
    return render(request, 'hello.html', {"name": "Django Method"})
    # return HttpResponse("Hello, Django!")