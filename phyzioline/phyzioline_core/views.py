from django.shortcuts import render
from django.http import Http404
from django.conf import settings
import os

def serve_frontend(request, path=''):
    """
    Serve static HTML files from the frontend_static directory.
    """
    if not path:
        path = 'index.html'
    
    # Normalize path
    if path.endswith('/'):
        path += 'index.html'
        
    # Try to find the file in website/
    # We use render to let Django find the file in TEMPLATES DIRS
    # which now includes frontend_static
    
    # List of prefixes to try
    prefixes = ['website', 'client-dashboard', '']
    
    for prefix in prefixes:
        if prefix:
            template_name = f'{prefix}/{path}'
        else:
            template_name = path
            
        # Check if file exists to avoid TemplateDoesNotExist spam/error
        # We construct the full path to check existence
        full_path = settings.BASE_DIR / 'frontend_static' / template_name
        if full_path.exists() and full_path.is_file():
            return render(request, template_name)

    # If not found as a template, it might be a static asset requested via this view
    # But assets should be handled by static view. 
    # If we get here, 404.
    raise Http404(f"Page not found: {path}")
