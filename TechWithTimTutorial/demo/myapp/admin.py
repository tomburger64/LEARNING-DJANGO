from django.contrib import admin
from .models import TodoItem #import the basic todo db model done in models.py

# Register your models here.
# models are the DB stuff (like the rows and fields attributes I made in models.py)
admin.site.register(TodoItem)
# any change done to the db models requires a "migration"
# a migration's like updating the db while keeping its existing data
# to do that, use CLI (https://youtu.be/nGIg40xs9e4?si=j1N4YRzGq5SdUUj8&t=932)