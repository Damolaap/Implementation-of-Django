from django.urls import path
from . import views 

urlpatterns = [
    path('blogs/', views.show_index),
    path('post/<int:id>/', views.show_post),
    path('contact/', views.show_contact),
    path('about/', views.show_about),
    path('category/<str:category>/', views.category),
]