from django.urls import path
from . import views

app_name = 'app_food'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/', views.item_detail, name='item_detail'),
]