from django.urls import path
from . import views

# LOGIN FOR "admin/" IS USER (for every field, mail empty)

# when we go to specified path (` "" `) (url)
# runs the views.home view or function (myapp\views.py) which returns an http response
urlpatterns = [
    path("", views.home, name="home"),
    path("todos/", views.todos, name='Todos')
]