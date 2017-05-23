from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from oscar.app import application
from django.http import HttpResponse
from oscar.views import handler500, handler404, handler403

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    # django admin is not officially supported by oscar - you should use the dashboard instead
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(application.urls)),
    # url(r'^brands/', include('customapp.apps.brandslider.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        url(r'^403$', handler403),
        url(r'^404$', handler404),
        url(r'^500$', handler500),
    ]
