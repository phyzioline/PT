"""
Main views for Phyzioline web interface
Server-side rendered Django templates
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    """
    API Root - Shows available API endpoints
    """
    return Response({
        'message': 'Welcome to Phyzioline API',
        'version': 'v1',
        'endpoints': {
            'auth': {
                'register': reverse('accounts:register', request=request, format=format),
                'login': reverse('accounts:login', request=request, format=format),
                'logout': reverse('accounts:logout', request=request, format=format),
                'refresh': reverse('accounts:token_refresh', request=request, format=format),
            },
            'profile': reverse('accounts:profile', request=request, format=format),
            'jobs': '/api/v1/jobs/',
            'marketplace': '/api/v1/marketplace/',
            'courses': '/api/v1/courses/',
            'clinics': '/api/v1/clinics/',
            'sessions': '/api/v1/sessions/',
            'feed': '/api/v1/feed/',
            'ads': '/api/v1/ads/',
            'crm': '/api/v1/crm/',
            'ai': '/api/v1/ai/',
            'equivalency': '/api/v1/equivalency/',
            'global-stats': '/api/v1/global-stats/',
        },
        'documentation': 'See API_ENDPOINTS.md for detailed documentation'
    })

# Web Views (Server-side rendering)

def home(request):
    """Homepage with feed"""
    context = {
        'page_title': 'Home - Phyzioline'
    }
    return render(request, 'home.html', context)

def marketplace(request):
    """Marketplace page"""
    context = {
        'page_title': 'Marketplace - Phyzioline'
    }
    return render(request, 'marketplace.html', context)

def courses(request):
    """Courses page"""
    context = {
        'page_title': 'Courses - Phyzioline'
    }
    return render(request, 'courses.html', context)

def jobs(request):
    """Jobs page"""
    context = {
        'page_title': 'Jobs - Phyzioline'
    }
    return render(request, 'jobs.html', context)

def sessions(request):
    """Home sessions booking page"""
    context = {
        'page_title': 'Book a Session - Phyzioline'
    }
    return render(request, 'sessions.html', context)

def clinics(request):
    """Clinic ERP page"""
    context = {
        'page_title': 'Clinic Management - Phyzioline'
    }
    return render(request, 'clinics.html', context)

def global_stats(request):
    """Global statistics page"""
    context = {
        'page_title': 'Global Statistics - Phyzioline'
    }
    return render(request, 'global_stats.html', context)

@login_required
def profile(request):
    """User profile page"""
    context = {
        'page_title': 'My Profile - Phyzioline'
    }
    return render(request, 'profile.html', context)

