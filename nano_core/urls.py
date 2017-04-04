from django.conf.urls import include, url

import views

urlpatterns = [
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
        views.home_files, name='home-files'),
]


urlpatterns += [
    url(r'^$', views.home, name = "home"),
    url(r'^news$', views.news, name = "news"),
    url(r'^members/$', views.members, name = "members"),
    url(r'^members/(?P<member_id>\w+)/$', views.members, name = "members_show"),
    url(r'^publications/$', views.publications, name = "publications"),
    url(r'^contact/$', views.contact, name = "contact"),
    url(r'^search/$', views.search, name = "search"),
]
