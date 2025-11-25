from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import EquivalenceRequirement, ExploreDataPoint, Ad
from .serializers import EquivalenceRequirementSerializer, ExploreDataPointSerializer, AdSerializer
from django.shortcuts import render
from rest_framework import status
from django.http import Http404

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
    """Return an HTMX fragment containing latest explore datapoints (demo)."""
    points = ExploreDataPoint.objects.order_by('-year')[:10]
    return render(request, 'marketing/_htmx_feed_fragment.html', {'points': points})


def htmx_like(request):
    """Simple demo endpoint to respond to HTMX like POSTs. Returns a small fragment."""
    label = request.POST.get('label', 'item')
    return render(request, 'marketing/_htmx_like_fragment.html', {'label': label})
    # Allow anonymous access for read-only dev purposes
    permission_classes = [AllowAny]


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
