from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', include('app_Login.urls', namespace='login')),
    path('dashboard/', include('app_Dashboard.urls', namespace='dashboard')),
    path('comments/', include('app_Comments.urls', namespace='comments')),
    path('newsletter/', include('app_NewSletter.urls', namespace='newsletters')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
