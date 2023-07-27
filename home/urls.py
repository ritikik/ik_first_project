from django.urls import path
from home import views

urlpatterns = [
    path('',views.landingPage),
    path('sendData',views.sendData),
    path('getData',views.getData),
    path('delete', views.delete),
    path('edit', views.edit),
    path('updateData',views.updateData),
    path('signUp',views.signUp),
    path('login/', views.user_login, name='login'),
]
