from django.shortcuts import render, HttpResponse
from .models import TodoItem # importing todos so it can be passed

# # ↓ can return html template or some http
# def home(request):
#     return HttpResponse("Hello World!")

# function that takes a "request" parameter (HTTP request)
# return render function, returns HTTP response
def home(request):
    return render(request, "home.html")

# passing a dictionnary as render's param, goes through the db entries
# instance var items made to get all the model's data (functions from django, not classic dom)
def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})