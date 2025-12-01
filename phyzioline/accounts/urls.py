from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from phyzioline_core.views import api_root
from .views import (
    RegisterView,
    CustomTokenObtainPairView,
    logout_view,
    ProfileView,
    PublicProfileView,
)

app_name = 'accounts'

urlpatterns = [
    # API Root - Must be first
    path('', api_root, name='api_root'),
    
    # Authentication endpoints
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('auth/logout/', logout_view, name='logout'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Profile endpoints
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/<int:id>/', PublicProfileView.as_view(), name='public_profile'),
]

