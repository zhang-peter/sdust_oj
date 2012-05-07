from django.conf.urls.defaults import patterns, include, url
from sdust_oj.views import test_view
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sdust_oj.views.home', name='home'),
    # url(r'^sdust_oj/', include('sdust_oj.foo.urls')),
    url(r'^auth/', include('sdust_oj.auth.urls')),
    url(r'^test/', test_view, name="test_view"),
)
