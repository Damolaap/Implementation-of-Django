from django.urls import path
from . import views 
#query protocol
urlpatterns = [
    path('hello/', views.show_index),
    path('about-page/', views.show_about),
    path('contact-page/', views.show_contact),
    path('query-page/', views.show_query),
    path('word-search/', views.show_search),
    path('a-page/<int:num>', views.show_empty),
    path('delete/<int:id>',views.deletebio),
    path('update/<int:id>',views.update_bio),
    path('blog/', views.show_blog),
    path('blog/<int:id>',views.blog_detail),

]