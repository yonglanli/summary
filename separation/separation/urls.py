"""separation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from rest_framework.documentation import include_docs_urls
# 配置api路由
from rest_framework.routers import DefaultRouter
from backend.views import KeyWordViewSet, KeyWordTypeViewSet
router = DefaultRouter()
router.register(r'keyword', KeyWordViewSet, base_name='keyword')
router.register(r'keywortype', KeyWordTypeViewSet, base_name='keyword_type')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),  # 配置url的路径
    url(r'^docs/', include_docs_urls(title="简单的前后台Vue分离系统")),  # 配置url的文档
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
]
