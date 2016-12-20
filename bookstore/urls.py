
from django.conf.urls import url,include
from django.contrib import admin
from store.views import index, store

urlpatterns = [
	url(r'^$',index,name = "homepage"),
	url(r'^store/',include('store.urls'),name = 'store'),
    url(r'^admin/', admin.site.urls),
]
