from django.urls import path
from .views import (
    EquivalenceRequirementList,
    ExploreDataList,
    ModulesOverview,
    ModulesByName,
    ModuleItemDetail,
    AdsListCreate,
    AdDetail,
)

urlpatterns = [
    path('equivalence/', EquivalenceRequirementList.as_view(), name='equivalence-list'),
    path('explore/', ExploreDataList.as_view(), name='explore-list'),

    # Demo endpoints for quick testing/editor preview for all modules
    path('modules/', ModulesOverview.as_view(), name='modules-overview'),
    path('modules/<str:module_name>/', ModulesByName.as_view(), name='modules-by-name'),
    path('modules/<str:module_name>/<int:item_id>/', ModuleItemDetail.as_view(), name='module-item-detail'),
    # DB-backed ads endpoints
    path('ads/', AdsListCreate.as_view(), name='ads-list-create'),
    path('ads/<int:pk>/', AdDetail.as_view(), name='ads-detail'),
]
