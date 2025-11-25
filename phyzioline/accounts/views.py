from rest_framework import status, generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from .models import UserProfile
from .serializers import (
    RegisterSerializer, 
    UserProfileSerializer, 
    ProfileUpdateSerializer,
    UserSerializer
)


class RegisterView(generics.CreateAPIView):
    """
    API endpoint للتسجيل (Register)
    POST /api/v1/auth/register/
    """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        # إنشاء JWT tokens
        refresh = RefreshToken.for_user(user)
        
        # إرجاع بيانات المستخدم والـ tokens
        return Response({
            'status': 'success',
            'message': 'تم التسجيل بنجاح',
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'role': user.userprofile.role,
                'role_display': user.userprofile.get_role_display(),
            },
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        }, status=status.HTTP_201_CREATED)


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    API endpoint لتسجيل الدخول (Login)
    POST /api/v1/auth/login/
    """
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        
        if response.status_code == 200:
            # إضافة معلومات المستخدم للاستجابة
            user = User.objects.get(username=request.data.get('username'))
            response.data['user'] = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'role': user.userprofile.role,
                'role_display': user.userprofile.get_role_display(),
            }
            response.data['status'] = 'success'
            response.data['message'] = 'تم تسجيل الدخول بنجاح'
        
        return response


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def logout_view(request):
    """
    API endpoint لتسجيل الخروج (Logout)
    POST /api/v1/auth/logout/
    يتطلب: Authorization: Bearer <token>
    """
    try:
        refresh_token = request.data.get('refresh')
        if refresh_token:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({
                'status': 'success',
                'message': 'تم تسجيل الخروج بنجاح'
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'status': 'error',
                'message': 'refresh token مطلوب'
            }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({
            'status': 'error',
            'message': 'حدث خطأ أثناء تسجيل الخروج'
        }, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(generics.RetrieveUpdateAPIView):
    """
    API endpoint لعرض وتحديث ملف التعريف
    GET /api/v1/accounts/profile/ - عرض ملف التعريف الحالي
    PUT /api/v1/accounts/profile/ - تحديث ملف التعريف
    PATCH /api/v1/accounts/profile/ - تحديث جزئي
    """
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        """إرجاع ملف تعريف المستخدم الحالي"""
        return self.request.user.userprofile
    
    def get_serializer_class(self):
        """استخدام ProfileUpdateSerializer للتحديث"""
        if self.request.method in ['PUT', 'PATCH']:
            return ProfileUpdateSerializer
        return UserProfileSerializer


class PublicProfileView(generics.RetrieveAPIView):
    """
    API endpoint لعرض ملف تعريف عام (للعامة)
    GET /api/v1/accounts/profile/{id}/
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'
