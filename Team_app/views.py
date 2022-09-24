from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers
from .models import Team
from .serializers import TeamSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from Company_app.models import Company
from Company_app.serializers import CompanySerializer, TeamViewSerializer

# jwt authentication related imports
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.
class TeamViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

# handling create team requirement

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def createTeam_view(request, company_id):
    # check company exists or not
    try:
        required_company = Company.objects.get(UUID=company_id)
        serialized = CompanySerializer(required_company)
    except:
        return Response({"message": "no such Company Found"})
    # check if team uuid already exists
    try:
        team = Team.objects.get(UUID=request.data["UUID"])
        return Response({"message": "this team uuid already exists"})
    except:
        # means the team does not exist as it throws error
        new_team = Team(UUID=request.data["UUID"], CompanyID=required_company, Team_lead=request.data['Team_Lead'])
        new_team.save()
        print("new team added")
        serialized_team = TeamSerializer(new_team)
        return Response(serialized_team.data)


    # print(request.data["UUID"])
    # print(request.data['Team_Lead'])

    # return Response(serialized.data)
class ViewTeamSerializer(serializers.ModelSerializer):
    teams = TeamSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ['name']
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def teams_view(request):
    all_teams = Company.objects.all()
    serialized_team = TeamViewSerializer(all_teams, many=True)
    print("trigger test")
    return Response(serialized_team.data)