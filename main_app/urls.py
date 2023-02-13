from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('items', views.ItemsList.as_view(), name='index'),
    path('items/myitems/', views.MyItemsList.as_view(), name='items_myitems'),
    path('items/create/', views.ItemCreate.as_view(), name='item_create'),
    path('items/<int:pk>/update/', views.ItemUpdate.as_view(), name='item_update'),
    path('items/<int:pk>/delete/', views.ItemDelete.as_view(), name='item_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', views.Login.as_view()),
]

