from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:flight_id>', views.flight, name='flight'),
    path('forms/', views.forms_page, name="forms-page"),
]
