from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', views.index),
path('cat/<int:id>', views.bycat),
path('add/<int:id>', views.addtocart),
path('cview/<int:id>', views.viewcart),
path('delete/<int:id>', views.deletecart),
path('register', views.register),
]