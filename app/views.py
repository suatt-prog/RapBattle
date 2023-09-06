from django.shortcuts import render,HttpResponse

# Create your views here.
import os,requests
import openai
from googletrans import Translator

def main(request):
    return render(request,"index.html")
def makerequest(request):
    openai.api_key = ""
    translator = Translator()
    translated_text = translator.translate("Write a rap battle happenin between "+request.GET["firstPerson"]+" and "+request.GET["secondPerson"], dest=request.GET["language"]).text


    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
            "role": "user",
            "content": translated_text#"Write a rap battle happenin between "+request.GET["firstPerson"]+" and "+request.GET["secondPerson"]
            }
        ],
        temperature=0.8,
        max_tokens=1024
    )
    return render(request,"index.html",{"context":response["choices"][0]["message"]["content"]})
