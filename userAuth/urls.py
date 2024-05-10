from django.urls import path
from userAuth.views import register
from userAuth.views import login_user
from userAuth.views import logout_user
from . import views 

app_name = 'auth'

urlpatterns = [
path('register/', register, name='register'),
path('login/', login_user, name='login'),
path('logout/', logout_user, name='logout'),

]