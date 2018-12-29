"""
Definition of urls for BasicProject.
"""

from django.conf.urls import include, url
import first_app.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', BasicProject.views.home, name='home'),
    # url(r'^BasicProject/', include('BasicProject.BasicProject.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', first_app.views.index, name='index'),
    url(r'^home$', first_app.views.index, name='home'),
]
