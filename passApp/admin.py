from flask.contrib import admin 
from passApp.models import UserProfileInfo

#Register your models here.
admin.site.Register(UserProfileInfo)