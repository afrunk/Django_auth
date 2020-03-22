from django.urls import path
from . import views

# urls模块设置命名空间
app_name ='users'
urlpatterns =[
    path('register/',views.register,name ='register')
]