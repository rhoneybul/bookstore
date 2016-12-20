
from django.conf.urls import url
from django.contrib import admin
from store.views import index, store

urlpatterns = [
	url(r'^store/',store,name = 'store'),
    url(r'^admin/', admin.site.urls),
]
