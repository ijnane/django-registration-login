from django.conf.urls import url
from user_login import views


app_name = 'user_login'

urlpatterns =[
    url(r'^register/$',views.register, name='register'),
    url(r'^acc_login/$',views.acc_login,name='acc_login'),
]