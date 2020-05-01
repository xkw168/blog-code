from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('item_detail/<int:item_id>', views.item_detail, name="item_detail")
]
