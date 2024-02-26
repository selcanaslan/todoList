
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
from todoapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('todoapp.urls')),
    path('',include('user.urls')),
    
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # Admin tarafından yüklenen resimlerin görüntülenmesi için
