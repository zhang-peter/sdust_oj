from django.conf.urls.defaults import patterns, include, url
from cup_oj.views import test_view
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cup_oj.views.home', name='home'),
    # url(r'^cup_oj/', include('cup_oj.foo.urls')),
    url(r'^auth/', include('cup_oj.auth.urls')),
    url(r'^test/', test_view, name="test_view"),
)
