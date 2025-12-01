from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import EquivalenceRequirement, ExploreDataPoint, Ad
from .serializers import EquivalenceRequirementSerializer, ExploreDataPointSerializer, AdSerializer
from django.shortcuts import render
from rest_framework import status
from django.http import Http404, HttpResponse

# API لجلب متطلبات المعادلة
class EquivalenceRequirementList(generics.ListAPIView):
    queryset = EquivalenceRequirement.objects.all()
    serializer_class = EquivalenceRequirementSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = super().get_queryset()
        country_code = self.request.query_params.get('country')
        if country_code:
            queryset = queryset.filter(country_code=country_code.upper())
        return queryset


# API لجلب بيانات الاستكشاف
class ExploreDataList(APIView):
    """
    جلب بيانات الاستكشاف مع تجميع البيانات حسب نوعها والدولة.
    """
    def get(self, request, format=None):
        data_type = request.query_params.get('data_type')
        queryset = ExploreDataPoint.objects.all()
        
        if data_type:
            queryset = queryset.filter(data_type=data_type.upper())
            
        serializer = ExploreDataPointSerializer(queryset, many=True)
        
        # تجميع البيانات لتسهيل استخدامها في الرسوم البيانية في الفرونت إند
        data_by_type = {}
        for item in serializer.data:
            key = item['data_type']
            if key not in data_by_type:
                data_by_type[key] = []
            data_by_type[key].append({
                'country': item['country'],
                'value': item['value'],
                'year': item['year']
            })
            
        return Response(data_by_type)

def htmx_feed(request):
    """Return an HTMX fragment containing latest feed posts and ads."""
    from feed.models import Post
    from content.models import Ad
    import random

    # Fetch latest posts
    posts = list(Post.objects.filter(is_published=True).select_related('author__user').order_by('-created_at')[:20])
    
    # Fetch some ads
    ads = list(Ad.objects.filter(is_active=True)[:5])
    
    # Mix ads into posts (simple injection)
    feed_items = []
    ad_index = 0
    for i, post in enumerate(posts):
        feed_items.append({'type': 'post', 'data': post})
        # Inject an ad every 3 posts
        if (i + 1) % 3 == 0 and ad_index < len(ads):
            feed_items.append({'type': 'ad', 'data': ads[ad_index]})
            ad_index += 1
            
    return render(request, 'marketing/_htmx_feed_fragment.html', {'feed_items': feed_items})


def htmx_like(request):
    """Handle like toggle via HTMX."""
    from feed.models import Post, Like
    from django.shortcuts import get_object_or_404
    
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        if post_id and request.user.is_authenticated:
            post = get_object_or_404(Post, id=post_id)
            user_profile = request.user.userprofile
            
            like, created = Like.objects.get_or_create(user=user_profile, post=post)
            if not created:
                like.delete()
                post.likes_count = max(0, post.likes_count - 1)
                liked = False
            else:
                post.likes_count += 1
                liked = True
            post.save()
            
            return render(request, 'marketing/_htmx_like_fragment.html', {
                'post': post, 
                'liked': liked
            })
            
    return HttpResponse(status=204)


class ModulesOverview(APIView):
    """Return demo/sample items for each primary module to help frontend testing.

    This is intentionally lightweight (no DB) so you can test and edit data quickly.
    """
    permission_classes = [AllowAny]

    SAMPLE = {
        'accounts': [
            {'id': 1, 'username': 'alice', 'role': 'therapist'},
            {'id': 2, 'username': 'bob', 'role': 'client'},
        ],
        'marketplace': [
            {'id': 1, 'title': 'Therapy Mat', 'price': 49.99},
            {'id': 2, 'title': 'Exercise Band', 'price': 19.99},
        ],
        'jobs': [
            {'id': 1, 'title': 'Physio Therapist - Riyadh', 'company': 'HealthCo'},
            {'id': 2, 'title': 'Clinic Manager', 'company': 'Wellness Ltd'},
        ],
        'courses': [
            {'id': 1, 'title': 'Manual Therapy Basics', 'length_hours': 12},
            {'id': 2, 'title': 'Pediatric Rehab', 'length_hours': 8},
        ],
        'clinics': [
            {'id': 1, 'name': 'Al Noor Clinic', 'city': 'Jeddah'},
            {'id': 2, 'name': 'City Physio', 'city': 'Cairo'},
        ],
        'home_sessions': [
            {'id': 1, 'client': 'bob', 'scheduled': '2025-11-25T10:00:00Z'},
        ],
        'feed': [
            {'id': 1, 'title': 'New research on knee rehab', 'summary': 'A short summary'},
        ],
        'ads': [
            {'id': 1, 'title': 'Ad: New Clinic Opening', 'sponsor': 'HealthCo'},
        ],
        'ai_engine': [
            {'id': 1, 'name': 'GaitAnalysis v1', 'status': 'ready'},
        ],
        'crm': [
            {'id': 1, 'contact': 'Alice', 'notes': 'Follow up in 2 weeks'},
        ],
        'global_stats': [
            {'id': 1, 'metric': 'active_users', 'value': 1245},
        ],
        'library': [
            {'id': 1, 'title': 'Clinical Practice Guidelines', 'type': 'pdf'},
        ],
    }

    def get(self, request, format=None):
        return Response(self.SAMPLE)


class ModulesByName(APIView):
    permission_classes = [AllowAny]

    def get(self, request, module_name, format=None):
        data = ModulesOverview.SAMPLE
        items = data.get(module_name)
        if items is None:
            return Response({'detail': 'Module not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(items)


class ModuleItemDetail(APIView):
    permission_classes = [AllowAny]

    def get(self, request, module_name, item_id, format=None):
        data = ModulesOverview.SAMPLE
        items = data.get(module_name)
        if items is None:
            return Response({'detail': 'Module not found'}, status=status.HTTP_404_NOT_FOUND)
        for it in items:
            if int(it.get('id')) == int(item_id):
                return Response(it)
        return Response({'detail': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)


# Ads API (DB-backed)
class AdsListCreate(generics.ListCreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [AllowAny]


class AdDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [AllowAny]
