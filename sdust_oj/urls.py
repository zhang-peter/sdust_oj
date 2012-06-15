from django.conf.urls.defaults import patterns, include, url
from sdust_oj.views import test_view, index
from django.http import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sdust_oj.views.index', name='index'),
    # url(r'^sdust_oj/', include('sdust_oj.foo.urls')),
    url(r'^auth/', include('sdust_oj.auth.urls')),
    url(r'^problem/', include('sdust_oj.problem.urls')),
    url(r'^users/', include('sdust_oj.users.urls')),
    url(r'^test/', test_view, name="test_view"),
    url(r'^admin/', include('sdust_oj.admin.urls')),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )