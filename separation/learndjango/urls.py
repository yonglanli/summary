from django.conf.urls import url, include

from learndjango import views

app_name = "learndjango"


urlpatterns = [
    # TODO django学习
    # 系统信息
    url(r'^$', views.index),
    url(r'^system-manage/$', views.system_manage, name='system_manage'),  # 系统管理首页

]