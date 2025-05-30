from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('t_and_c/', views.terms_and_conditions, name='t_and_c'),
    path('about_us/', views.about_us, name='about_us'),
    path('services/<slug:service_type>/', views.services_view, name='services'),
]
