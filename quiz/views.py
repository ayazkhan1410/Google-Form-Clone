from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


class HomeAPIView(APIView):

    def get(self, request):
        return Response({
            "message":"Hello World"
        }, status=status.HTTP_200_OK)

    def post(self, request):
        pass

    def put(self, request):
        pass

    def patch(self, request):
        pass

    def delete(self, request):
        pass
