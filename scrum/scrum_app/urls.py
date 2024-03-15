from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Home-Page"),
    # path('<str:cert_id>')


]
