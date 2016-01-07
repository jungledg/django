from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
     url(r'^staff/','west.views.staff'),
)