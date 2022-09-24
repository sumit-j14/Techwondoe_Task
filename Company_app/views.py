from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Company
from .serializers import CompanySerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes

# jwt authentication related imports
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class CompanyViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    # @action(detail=True)
    # def company_name(self, request, pk=None):
    #     print("triggered")
    #     queryset = Company.objects.get(name=pk)
    #     serializer = CompanySerializer(queryset)
    #     return Response(serializer.data)

    # overriding to provide search by name functionality
    # def retrieve(self, request, pk):
    #     # pk is passed in url request
    #     if pk.isnumeric():
    #         # search by company id
    #         try:
    #             requested_company = Company.objects.get(pk=pk)
    #             print(requested_company)
    #             serialized = CompanySerializer(requested_company)
    #             return Response(serialized.data)
    #         except:
    #             # in case no such company is found
    #             # print("no content")
    #             return Response({"message": "no such company exists"}, status=status.HTTP_204_NO_CONTENT)
    #     else:
    #         # search by company name ( string )
    #         print("searching for company "+pk)
    #         try:
    #             requested_company = Company(name=pk)
    #             print(requested_company)
    #             serialized = CompanySerializer(requested_company)
    #             return Response(serialized.data)
    #         except:
    #             # in case no such company is found
    #             print("no content")
    #             return Response({"message": "no such company exists"}, status=status.HTTP_204_NO_CONTENT)
    #     return Response({})
@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def search_view(request, key):
    # print("test triggered")
    print("key is "+key)
    try:
        requested_company = Company.objects.get(name=key)
        serialized = CompanySerializer(requested_company)
        # print(requested_company)
        return Response(serialized.data)
    except:
        return Response({"message": "no such company exists"}, status=status.HTTP_204_NO_CONTENT)

