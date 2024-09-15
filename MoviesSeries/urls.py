from . import views
from django.urls import path

urlpatterns = [
    path('similarity/', views.similarity),
    path('webhook/', views.dialogflow_webhook),
]