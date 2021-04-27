from django.urls import path
from .views import HomeView, About


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', About, name='about')
]