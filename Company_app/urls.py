from django.urls import path
from .views import CompanyViewSet, search_view
urlpatterns = [
    path('', CompanyViewSet.as_view),
    # search by company name
    # path('search/<c_name>', search_view)
]