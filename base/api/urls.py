from django.urls import path
from . import views

urlpatterns = [
    path('',views.Routes),
    path('banks/',views.getbankList),
    path('banks/<str:pk>',views.getBank),
]