from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:pk>/delete', views.delete, name="delete"),
    path('<int:pk>/update', views.update, name="update"),

]