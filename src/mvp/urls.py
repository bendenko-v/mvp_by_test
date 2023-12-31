from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('core.urls.user')),
    path('posts/', include('core.urls.post')),
]
