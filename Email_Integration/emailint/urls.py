from django.urls import path
from .views import registrationForm, registrationSuccess

urlpatterns = [
    path('signup/', registrationForm, name='register'),
    path('success/', registrationSuccess, name='success'),

]