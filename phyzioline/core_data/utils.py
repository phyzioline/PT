"""
Utility Functions مشتركة
"""
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework import status


def paginate_queryset(queryset, request, page_size=20):
    """تقسيم النتائج إلى صفحات"""
    paginator = Paginator(queryset, page_size)
    page_number = request.query_params.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    return {
        'count': paginator.count,
        'next': page_obj.next_page_number() if page_obj.has_next() else None,
        'previous': page_obj.previous_page_number() if page_obj.has_previous() else None,
        'results': page_obj.object_list
    }


def success_response(data=None, message="تمت العملية بنجاح", status_code=status.HTTP_200_OK):
    """إرجاع استجابة نجاح موحدة"""
    response_data = {
        'status': 'success',
        'message': message,
    }
    if data is not None:
        response_data['data'] = data
    
    return Response(response_data, status=status_code)


def error_response(message="حدث خطأ", errors=None, status_code=status.HTTP_400_BAD_REQUEST):
    """إرجاع استجابة خطأ موحدة"""
    response_data = {
        'status': 'error',
        'message': message,
    }
    if errors:
        response_data['errors'] = errors
    
    return Response(response_data, status=status_code)

