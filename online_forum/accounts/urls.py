from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('list/', home, name='list'),      # placeholder
    path('create/', home, name='create'),  # placeholder
    path('details/', home, name='details'),# placeholder
]
