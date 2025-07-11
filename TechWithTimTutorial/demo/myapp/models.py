from django.db import models

# Create your models (databases) here.
# this is made to create DBs using code (ORM)
# converts the code into set schemes for supported DBs (SQLite, Potgre, Mongo, etc)

# todoitem db
class TodoItem(models.Model):
    title = models.CharField(max_length=200) #title row, contains a char field
    completed = models.BooleanField(default=False) # completed row, contains bool field
# this needs to be registered in the "admin panel" once done