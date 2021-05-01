from django.urls import path

from .views import registerView, logoutView, loginView

urlpatterns = [
    path('register/', registerView.as_view(), name='register'),
    path('logout/', logoutView, name='logout'),
    path('login/', loginView.as_view(), name='login')
]
