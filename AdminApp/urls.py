from django.conf.urls import url

from AdminApp import views

urlpatterns =[
    url(r'^login/',views.login),
    url(r'^checklogin/',views.checklogin,name='checklogin'),
    # 图片验证码
    url(r'^get_code/', views.get_code, name='get_code'),
    url(r'^home/', views.home),
]