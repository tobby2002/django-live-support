#from django.conf.urls import patterns, include, url
from django.conf.urls import url, include
from django.views.generic import TemplateView

from .views import iframe

from django.contrib import admin
admin.autodiscover()

# urlpatterns = patterns('',
#     url(r'^admin/', include(admin.site.urls)),
#     url('^iframe/', 'demo.views.iframe'),
#     url('^', include('live_support.urls')),
# )

urlpatterns = [
    url(r'^', iframe),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^iframe/', iframe),
    #url(r'^', include('live_support.urls')),
]