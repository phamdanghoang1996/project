"""untitled URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include, url
from django.contrib import admin
from home import views

urlpatterns = (
	url(r'^admin/', admin.site.urls),
	url(r'^adidas/', views.adidas, name='adidas'),
	url(r'^nike/', views.nike, name='nike'),
	url(r'^bitis/', views.bitis, name='bitis'),
	url(r'^non/', views.non, name='non'),
	url(r'^lienhe/', views.lienhe, name='lienhe'),
	url(r'^gioithieu/', views.gioithieu, name='gioithieu'),
	url(r'^tuyendung/', views.tuyendung, name='tuyendung'),
	url(r'^vanchuyen/', views.vanchuyen, name='vanchuyen'),
	url(r'^chinhsachdoitra/', views.chinhsachdoitra, name='chinhsachdoitra'),
	url(r'^chinhsachbaohanh/', views.chinhsachbaohanh, name='chinhsachbaohanh'),
	url(r'^doitaccungcap/', views.doitaccungcap, name='doitaccungcap'),
	url(r'^detail/(?P<id>[0-9]+)/$', views.detail, name='detail')
)
