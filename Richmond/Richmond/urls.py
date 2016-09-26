"""Richmond URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
# custom
from index.views import index_view
from trade.views import select_stock_view, stock_view, add_trade, trade_record_view
from players.views import login_view, login, register_view, register, user_view

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', index_view),
	url(r'^trade/$', select_stock_view),
	url(r'^stock/$', stock_view),
	url(r'^addTrade/$', add_trade),
	url(r'^accounts/login/$', login_view),
	url(r'^accounts/login/register/$', register_view),
	url(r'^login/$', login),
	url(r'^register/$', register),
	url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',{'next_page': '/accounts/login'}),
	url(r'^tradeRecord/$', trade_record_view),
	url(r'^userList/$', user_view)
]
