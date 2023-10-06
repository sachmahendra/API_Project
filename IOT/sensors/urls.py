from django.urls import path

from . import views

urlpatterns = [
    path('postsensorData/',views.postsensorData.as_view()),
    path('getsensorData/', views.getsensorData.as_view()),
    path('getsensorData/<sensorid>/', views.getsensorDataDetails.as_view()),
    path('updatesensorData/', views.updatesensorDataDetails.as_view()),
    path('deletesensorData/<sensor_id>/', views.deletesensorData.as_view()),
    path('notifyUser/',views.notifyUser.as_view()),
    
]
