from django.urls import path
from . import views

app_name = 'threads'

urlpatterns = [
    # CREATE
    path('create/', views.create_thread, name='create_thread'),
    
    # READ
    path('', views.thread_list, name='thread_list'),
    path('<int:thread_id>/', views.thread_detail, name='thread_detail'),
    
    # UPDATE
    path('<int:thread_id>/update/', views.update_thread, name='update_thread'),
    
    # DELETE
    path('<int:thread_id>/delete/', views.delete_thread, name='delete_thread'),
]