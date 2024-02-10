# Create App level routes
from django.urls import path
from . import views

# domain.com/first_app/
# urlpatterns = [
#     # Create Dynamic Route with type conversions
#     path('<int:num_page>/', views.num_page_view),
#     path('<str:topic>/', views.news_view, name='topic-page')
#     # path('<int:num1>/<int:num2>/', views.add_view)
# ]

urlpatterns = [
    path('', views.simple_view)
]