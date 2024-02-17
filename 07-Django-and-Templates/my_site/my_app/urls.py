from django.urls import path
from . import views

# Register the app namespace
# Used for URL names
app_name = 'my_app'

urlpatterns = [
    path('', views.example_view, name='example'),
    path('variable', views.variable_view, name='variable')
]