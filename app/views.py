from django.shortcuts import render,HttpResponse

# Create your views here.
import os
import openai


def sendRequest(request):
    return render(request,"index.html",{"context":makerequest()})
def makerequest():
    openai.api_key = "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"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[],
        temperature=0.8,
        max_tokens=1024
    )
    return response