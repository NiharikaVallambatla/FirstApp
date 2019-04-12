from django.conf.urls import url,include
from django.contrib import admin

from Home2Home import views as home_views


urlpatterns = [
    url(r'^$', home_views.home.as_view(), name='home'),
    url(r'^listing/(?P<id>\d+)/', home_views.showItems,name='showItems'),
    url(r'^delete/(?P<id>\d+)/', home_views.delete_task,name='del_task'),
    url(r'^admin/', admin.site.urls),
]