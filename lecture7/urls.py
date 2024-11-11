from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home_page"),
    path('hello/<str:name>', views.hello, name="hello_page"),
    path('hello/', views.hello_, name="hello_page_"),
    path('hi/', views.hi, name="hello_page"),
    path('hi/<str:name>', views.hi, name="hi_page"),
]
