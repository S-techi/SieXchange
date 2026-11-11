from django.urls import path
from . import views

urlpatterns = [
    path('error/',views.error, name = 'error'),
    path('blogDetails/',views.blogDetails, name = 'blogDetails'),
    path('blog/',views.blog, name = 'blog'),
    path('',views.index, name = 'index'),
    path('portfolio/',views.portfolioDetails, name = 'portfolioDetails'),
    path('service/',views.serviceDetails, name = 'serviceDetails'),
    path('starterPage/',views.starterPage, name = 'starterPage'),
    path('show/',views.show, name = 'show'),
]
