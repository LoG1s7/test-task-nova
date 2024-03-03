from rest_framework.authtoken import views
from django.urls import path
from .views import upload_file

urlpatterns = [
    path('upload_file/', upload_file),
    path('api-token-auth/', views.obtain_auth_token),
]
