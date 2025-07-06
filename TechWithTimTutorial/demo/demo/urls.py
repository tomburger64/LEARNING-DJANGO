from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # ↓ everytime ` "" ` is reached in the url, will forward all urls into myapp\urls.py
    # `""` could be replaced with "myapp/" for example
    path('', include("myapp.urls"))
]
