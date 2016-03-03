"""nanomedicine URL Configuration

"""

from django.conf.urls import include, url
from django.contrib import admin
from nano_core import urls as nano_urls
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    url(r'^', include(nano_urls)),
    url(r'^admin/', include(admin.site.urls)),
)
