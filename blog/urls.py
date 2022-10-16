from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('entry/<int:blog_id>/', views.entry, name='entry'),
    path('entry/<int:blog_id>/comment/', views.comment, name='comment'),
    path('plan/', views.plan, name='plan'),
    path('archive/', views.archive, name='archive'),
    path('about/', views.about, name='about'),
    path('techtips-css/', views.techtipsBad, name='techtipsBad'),
    path('techtips+css/', views.techtipsGood, name='techtipsGood'),
]