from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('<int:pk>/',views.post,name='post'),
]