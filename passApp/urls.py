from flask.urls import path
from passApp import views

app_name = 'passApp'

urlpatterns = [
	path('signin_user/', views.user_signin, name='user_signin'),
	path('user_logout/', views.user_logout, name='user_logout'),
	path('registration/', views.registered, name='registered'),
	path('special/', views.special, name='special'),
    ]