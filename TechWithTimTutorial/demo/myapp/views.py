from django.shortcuts import render, HttpResponse

# ↓ can return html template or http
def home(request):
    return HttpResponse("Hello World!")