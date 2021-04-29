## Accessing students records using django rest api
### We are going to see how to create rest api in Python using django rest api

Section 1:
Install the all the dependency which are mention in the requirement.txt

Secton 2:
Step 1:

Create the project using the below command
```
django-admin startproject project_name 

example: django-admin startproject student

```

Test it(project created successfully or not) using the below command 
```
python manage.py runserver

April 28, 2021 - 18:52:17
Django version 3.2, using settings 't.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
Just copy-paste http://127.0.0.1:8000/ this any browser(Internet Explorer, Google Chrome, Mozilla Firefox ...)

You will see this 
![](images/1.png)
<br><br>
Step 2:

Now, Create the app using the below command
```
python manage.py startapp app_name 

example: python manage.py startapp api

```
Step 3:
Now, list the app and rest_framework in setting.py file 

When you open you will see this
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
You must need to list app_name and rest_framework
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',
]
```
<br><br>
Step 4:
Now open models.py and create your table
```
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    school = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
```
<br><br>
Step 5:
After creating the table open admin.py file to list the table in the admin panel 

```
from django.contrib import admin
from .models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','school','address']
```

Open your terminal migrate the table into database 
```
python manage.py makemigrations
```
after that
```
python manage.py migrate
```
Note: if you change anything in the table please run **python manage.py migrate** command

Create superuser 
```
python manage.py createsuperuser
```
password(must) other(if you want)

![](images/2.png)

Step 5:
Now again run the server
```
python manage.py runserver
```

and go to admin url 

```
http://127.0.0.1:8000/admin/

```
<br><br>
Step 6:
click the right side of the students and insert the record to it

Step 7:
open views.py file
```
from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets
# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```
step 8:
First create the serializers.py file in the app
```
from django.db import models
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Student
        fields =['id','name','roll','school','address']
```

Step 9:
Now we will build url with the help of routes, open urls.py file 
```
from django.contrib import admin
from django.db import router
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

router= DefaultRouter()

router.register('student', views.StudentViewSet, basename='student')

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',include(router.urls)),
   
]
```
