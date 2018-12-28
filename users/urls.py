# -*- coding:utf-8 -*-
from django.urls import path,include,re_path
from . import views

urlpatterns = [
	# 登录页面
	re_path(r'^$', views.login_view, name='login'),
	#注销
	re_path(r'^logout/$',views.logout_view,name='logout'),
	# 注册界面
	re_path(r'register/$',views.register,name='register'),
	
 ]
