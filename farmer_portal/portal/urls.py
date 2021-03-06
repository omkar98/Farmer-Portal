from django.urls import path, include
from . import views as portal_views
from farmers import views as farmer_views


urlpatterns = [
    path('', portal_views.home , name='portal-home'),
    path('farmer/', include('farmers.urls')),
    path('fpo/', include('fpo.urls')),
    path('buyer/', include('buyer.urls')),
    path('admin_portal/', include('admin_portal.urls')),
    path('service/', include('services.urls')),
    path('buyer/', include('buyer.urls')),
    path('admin_portal/', include('admin_portal.urls')),
    path('login/', portal_views.login, name='login'),
    path('view_post/', portal_views.view_post, name='view_post'),
    path('translate/', portal_views.translate, name='translate'),
]
