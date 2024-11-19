from django.urls import path

from . import views

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('add/', views.contact_add, name='contact_add'),
    path('delete/<int:id>/', views.contact_delete, name='contact_delete'),

]