from django.urls import path, include
from .views import index, delete

app_name = 'calories_tracker'
urlpatterns = [
    path('', index, name="index"),
    path('delete/<int:id>', delete, name="delete"),
    path('accounts/', include('django.contrib.auth.urls')),

]