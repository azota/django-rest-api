import imp
from pickle import GET
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse("<h1>Hello, world!</h1>")

def auth_token(request):
    return HttpResponse("{'token':'fdsafdsaj;fdsfsdaeifdsaj;fjadsfdsj;a','userid':'azota'}}")



from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizeSerializer
import random

@api_view(['GET'])
def helloApi(request):
    return Response('hello world!!')

@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizs = Quiz.objects.all()
    randomQuizs = random.sample(list(totalQuizs), id)
    serializer = QuizeSerializer(randomQuizs, many=True)
    return Response(serializer.data)

