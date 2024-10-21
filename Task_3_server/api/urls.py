from django.urls import path
from . import views

urlpatterns = [
    path('inverse/', views.inverse, name='inverse_create'),
    path('unstable/', views.unstable, name='unstable_create'),
]