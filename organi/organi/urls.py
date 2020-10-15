from django.contrib import admin
from django.urls import path, include
# For media Profile
from django.conf import settings
from django.contrib.staticfiles.urls import  staticfiles_urlpatterns,static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Shop.urls')),
    path('account/',include('App_Login.urls')),
    path('shop/',include('order_app.urls'))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)