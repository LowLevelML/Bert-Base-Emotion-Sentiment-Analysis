from django.http import HttpResponse
from django.shortcuts import render


def homePageView(request):
    return HttpResponse("Hello, World!")

@api_view(['POST'])
def postData(request):
    data = request.data
    sentence = data['Sentence']
    