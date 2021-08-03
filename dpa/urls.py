from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import debug_toolbar
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('sales/', include('sales.urls')),
    path('', RedirectView.as_view(url="/accounts/login/"))
]   
    
if settings.DEBUG:
    urlpatterns.append(path('debug/', include(debug_toolbar.urls)))
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
