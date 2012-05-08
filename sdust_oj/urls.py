from django.conf.urls.defaults import patterns, include, url
from sdust_oj.views import test_view, index
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sdust_oj.views.index', name='index'),
    # url(r'^sdust_oj/', include('sdust_oj.foo.urls')),
    url(r'^auth/', include('sdust_oj.auth.urls')),
    url(r'^problem/', include('sdust_oj.problem.urls')),
    url(r'^test/', test_view, name="test_view"),
    url(r'^admin/', include('sdust_oj.admin.urls')),
)
