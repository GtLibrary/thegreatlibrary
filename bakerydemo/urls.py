from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from django.conf.urls import url

import debug_toolbar
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.contrib.sitemaps.views import sitemap
from wagtail.core import urls as wagtail_urls

from bakerydemo.art import views as art_views
from bakerydemo.nft import views as nft_views
from bakerydemo.search import views as search_views
from bakerydemo.frontend import views as frontend_views
from .api import api_router

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.base import TemplateView
from bakerydemo.mobileapp import views as frontendapi_views
from rest_framework import routers
# from bakerydemo.base import views
#from froala_editor import views

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('django-admin/', admin.site.urls),

    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),

    path('search/', search_views.search, name='search'),

    url('^art/testalice/', csrf_exempt(art_views.testalice), name='testalice'),
    url('^art/testhtml/', csrf_exempt(art_views.testhtml), name='testhtml'),
    url('^art/testepub/', csrf_exempt(art_views.testepub), name='testepub'),
    url('^art/myopenai/', csrf_exempt(art_views.myopenai), name='myopenai'),
    url('^art/chat/', csrf_exempt(art_views.chat), name='chat'),
    url('^art/load_chat/', csrf_exempt(art_views.load_chat), name='load_chat'),

    url('^art/serialtest/', art_views.serialtest, name='serialtest'),
    url('^art/style.css', art_views.styles, name='styles'),
    url('^art/paper.jpg', art_views.paper, name='paper.jpg'),
    url('^art/emboss.png', art_views.emboss, name='emboss.png'),
    url('^art/images/', art_views.images, name='00000.jpeg'),
    url('^art/price/', art_views.price, name='price'),
    #url('^art/MUMBAIMEMECODE/', art_views.MUMBAIMEMECODE, name='MUMBAIMEMECODE'),
    url('^manifest.webmanifest', art_views.manifest, name='manifest.webmanifest'),
    url('^index.html', art_views.index, name='index.html'),
    url('^service-worker.js', art_views.serviceworker, name='service-worker.js'),
    path('art/', art_views.art, name='art'),

    url('^nft/', nft_views.nft, name='nft'),
    url('^contract/', nft_views.contractMetadata, name='contract'),
    url('^usage/', nft_views.usage, name='usage'),

    path('sitemap.xml', sitemap),
    path('api/v2/', api_router.urls),
    path('__debug__/', include(debug_toolbar.urls)),

    #path('djrichtextfield/', include('djrichtextfield.urls')),

    ### FOR REACT ###
    path('api/', include('bakerydemo.mobileapp.urls')),
	url(r'^api/art/$', frontendapi_views.art),
	# url(r'^api/home', frontendapi_views.home),
	# url(r'^api/getproducts', frontendapi_views.home),
	# url(r'^api/mobileapp/(?P<pk>[0-9]+)$', views.mobileapp_detail),
    #path('home/', include('bakerydemo.frontend.urls')),

    # url(r'^getData/', frontend_views.get_data),
    url(r'mobileapp', TemplateView.as_view(template_name="mobilehome.html"), name="mobilehome"),





    #url(r'^froala_editor/', include('froala_editor.urls')),


]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.views.generic import TemplateView
    from django.views.generic.base import RedirectView

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path(
            'favicon.ico', RedirectView.as_view(
                url=settings.STATIC_URL + 'img/bread-favicon.ico'
            )
        )
    ]

    # Add views for testing 404 and 500 templates
    urlpatterns += [
        path('test404/', TemplateView.as_view(template_name='404.html')),
        path('test500/', TemplateView.as_view(template_name='500.html')),
    ]

urlpatterns += [
    path('', include(wagtail_urls)),
]
