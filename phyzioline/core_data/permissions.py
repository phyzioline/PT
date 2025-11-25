"""
Custom Permission Classes للتحكم في الصلاحيات بناءً على الأدوار
"""
from rest_framework import permissions
from accounts.models import UserProfile


class IsDoctor(permissions.BasePermission):
    """السماح للأطباء فقط"""
    def has_permission(self, request, view):
        return (
            request.user and
            request.user.is_authenticated and
            hasattr(request.user, 'userprofile') and
            request.user.userprofile.role == 'doctor'
        )


class IsSpecialist(permissions.BasePermission):
    """السماح للأخصائيين فقط"""
    def has_permission(self, request, view):
        return (
            request.user and
            request.user.is_authenticated and
            hasattr(request.user, 'userprofile') and
            request.user.userprofile.role == 'specialist'
        )


class IsVendor(permissions.BasePermission):
    """السماح للموردين فقط"""
    def has_permission(self, request, view):
        return (
            request.user and
            request.user.is_authenticated and
            hasattr(request.user, 'userprofile') and
            request.user.userprofile.role == 'vendor'
        )


class IsCompany(permissions.BasePermission):
    """السماح للشركات/المراكز الطبية فقط"""
    def has_permission(self, request, view):
        return (
            request.user and
            request.user.is_authenticated and
            hasattr(request.user, 'userprofile') and
            request.user.userprofile.role == 'company'
        )


class IsTrainer(permissions.BasePermission):
    """السماح للمدربين/المحاضرين فقط"""
    def has_permission(self, request, view):
        return (
            request.user and
            request.user.is_authenticated and
            hasattr(request.user, 'userprofile') and
            request.user.userprofile.role == 'trainer'
        )


class IsTrainer(permissions.BasePermission):
    """السماح للمدربين/المحاضرين فقط"""
    def has_permission(self, request, view):
        return (
            request.user and
            request.user.is_authenticated and
            hasattr(request.user, 'userprofile') and
            request.user.userprofile.role == 'trainer'
        )


class IsAdmin(permissions.BasePermission):
    """السماح للمسؤولين فقط"""
    def has_permission(self, request, view):
        return (
            request.user and
            request.user.is_authenticated and
            (
                request.user.is_staff or
                (hasattr(request.user, 'userprofile') and request.user.userprofile.role == 'admin')
            )
        )


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permission مخصص: السماح للمالك فقط بالتعديل، والقراءة للجميع
    """
    def has_object_permission(self, request, view, obj):
        # القراءة مسموحة للجميع
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # الكتابة مسموحة للمالك فقط
        if hasattr(obj, 'user'):
            return obj.user == request.user
        elif hasattr(obj, 'company'):
            return obj.company.user == request.user
        elif hasattr(obj, 'vendor'):
            return obj.vendor.user == request.user
        elif hasattr(obj, 'author'):
            return obj.author == request.user
        
        return False


class IsCompanyOrAdmin(permissions.BasePermission):
    """السماح للشركات والمسؤولين فقط"""
    def has_permission(self, request, view):
        if not (request.user and request.user.is_authenticated):
            return False
        
        if not hasattr(request.user, 'userprofile'):
            return False
        
        role = request.user.userprofile.role
        return role == 'company' or request.user.is_staff or role == 'admin'


class IsSpecialistOrAdmin(permissions.BasePermission):
    """السماح للأخصائيين والمسؤولين فقط"""
    def has_permission(self, request, view):
        if not (request.user and request.user.is_authenticated):
            return False
        
        if not hasattr(request.user, 'userprofile'):
            return False
        
        role = request.user.userprofile.role
        return role == 'specialist' or request.user.is_staff or role == 'admin'

