from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'screenshot_uploader.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('file_upload.urls')),
    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
