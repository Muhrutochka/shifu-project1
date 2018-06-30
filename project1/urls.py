"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic.base import TemplateView
from firstapp.views import addArticles, articles, cnt, title, adminka, editArticles, delArticles
admin.autodiscover()
app_name = 'firstapp'

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    re_path('^admin_tools/', include('admin_tools.urls')),
    path('admin1/', admin.site.urls),
    path('admin/', adminka),
    path('admin/articles/', articles),
    path('admin/articles/add/', addArticles),
    path('', title),
    re_path('^admin/articles/edit/(?P<x>\w+)/$', editArticles),
    re_path('^admin/articles/delete/(?P<x>\w+)/$', delArticles),
    re_path('^admin/articles/(?P<x>\w+)/$', cnt),
    re_path('^articles/(?P<x>\w+)/$', cnt),
    re_path(r'^accounts/', include('allauth.urls')),
    re_path(r'^$', TemplateView.as_view(template_name='plain/example/index.html'), name='home'),
    re_path(r'^accounts/profile/$', TemplateView.as_view(template_name='plain/example/profile.html')),
]