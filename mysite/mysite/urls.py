from django.conf.urls import url,include
from django.contrib import admin

from Home2Home import views as home_views


urlpatterns = [
    url(r'^$', home_views.home.as_view(), name='home'),
    url(r'^listing/([0-9]+)/', home_views.showItems1,name='items_all'),
    url(r'^admin/', admin.site.urls),
]
#(?P<name>\d+)/$