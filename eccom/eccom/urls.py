from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core.views import frontpage, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('userprofile.urls')),
    path('', frontpage, name='frontpage'),
    path('about/', about, name='about'),
    path('', include('store.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
