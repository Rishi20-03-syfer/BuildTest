from django.shortcuts import render
from dotenv import dotenv_values
import google.generativeai as genai
from .models import Prompt
# Create your views here.
response = ""
try:
    api_key = dotenv_values('.env')
    genai.configure(api_key="AIzaSyD5NMUH15XM9nbZKcyePE60EliMc86owRw")
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    print(f"Error :Api key not found {e}")

def index(request):
    if request.method == "POST":
        text = request.POST.get("text")
        response = text_to_text(text)
        promptObj = Prompt.objects.create(text=text)
    else:
        response = "No text found"
    return render(request,"Index.html",context={"response":response})

def text_to_text(text):
    global model
    response = model.generate_content(text)
    return response.text

