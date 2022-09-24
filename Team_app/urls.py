from django.urls import path
from .views import CompanyViewSet

urlpatterns = [
    path('', CompanyViewSet.as_view)
]