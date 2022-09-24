
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Company_app.views import CompanyViewSet, search_view
from Team_app.views import TeamViewSet
from Team_app.views import createTeam_view, teams_view
from rest_framework.authtoken import views

# jwt related imports
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# router for companies
router = DefaultRouter()
router.register('', CompanyViewSet, basename='Company')

# router for teams
router2 = DefaultRouter()
router2.register('', TeamViewSet, basename='Team')



# url patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('CompanySearch/<key>', search_view),
    path('Company/', include(router.urls)),
    path('CreateTeam/<company_id>', createTeam_view),
    path('Team/', include(router2.urls)),
    path('GetTeams/', teams_view),

    # test paths ( not to be used in this project )
    # for creating new token as per django default token authentication
    path('api-token-auth/', views.obtain_auth_token),

    # jwt related routes
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
