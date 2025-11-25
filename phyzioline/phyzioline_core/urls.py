"""
URL configuration for phyzioline_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Marketing / core website (fast launch using Django templates)
    path('', TemplateView.as_view(template_name='marketing/index.html'), name='home'),
    path('admin/', admin.site.urls),
    # JWT Auth (Simple JWT)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # API URLs
    path('api/v1/', include('accounts.urls')),
    path('api/v1/jobs/', include('jobs.urls')),
    path('api/v1/marketplace/', include('marketplace.urls')),
    path('api/v1/courses/', include('courses.urls')),
    path('api/v1/clinics/', include('clinics.urls')),
    # Content endpoints (Equivalence & Explore)
    path('api/v1/content/', include('content.urls')),
    # HTMX demo endpoint
    path('htmx/feed/', include('content.urls_htmx')),
    path('api/v1/sessions/', include('home_sessions.urls')),
    path('api/v1/feed/', include('feed.urls')),
    path('api/v1/ads/', include('ads.urls')),
    path('api/v1/ai/', include('ai_engine.urls')),
    path('api/v1/crm/', include('crm.urls')),
    path('api/v1/equivalency/', include('equivalency.urls')),
    path('api/v1/global-stats/', include('global_stats.urls')),
    path('api/v1/payments/', include('payments.urls')),
]

# إضافة Media files في وضع التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
