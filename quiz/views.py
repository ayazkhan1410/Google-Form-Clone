from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
import traceback


class ChoiceAPIView(APIView):

    def get(self, request):
        try:
            choices = Choice.objects.all()
            serializer = ChoiceSerializer(choices, many=True)
            return Response({
                "Data":serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            traceback.print_exc()
            return Response({
                "Error Message": "Something went wrong",
                "Error":str(e)
            },status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            data = request.data

            if isinstance(data, list):
                serializer = ChoiceSerializer(many=True, data=data)
            else:
                serializer = ChoiceSerializer(data=data)

            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({
                    "data":serializer.data,
                    'message':"Choices created successfully"
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'error':serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            traceback.print_exc()
            return Response({
                "Error Message": "Something went wrong",
                "Error":str(e)
            },status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        data = request.data
        choice_id = data.get("id")

        if not choice_id:
            return Response("Choice ID is required")
    
        print("CHOICE ID ============================")
        print(choice_id)

        try:  
            choice_obj = Choice.objects.get(id = choice_id)
        except Choice.DoesNotExist as e:
            return Response({
                "Error Message": "Something went wrong",
                "Error":str(e)
            },status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
            serializer = ChoiceSerializer(choice_obj, data = data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({
                    'Message':"Choice Updated Successfully",
                    "Data":serializer.data
                },status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'error':serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            traceback.print_exc()
            return Response({
                "Error Message": "Something went wrong",
                "Error":str(e)
            },status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, *args, **kwargs):
        data = request.data
        choice_id = data.get("id")

        if not choice_id:
            return Response("Choice ID is required")
    
        print("CHOICE ID ============================")
        print(choice_id)

        try:  
            choice_obj = Choice.objects.get(id = choice_id)
        except Choice.DoesNotExist as e:
            return Response({
                "Error Message": "Something went wrong",
                "Error":str(e)
            },status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
            serializer = ChoiceSerializer(choice_obj, data = data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({
                    'Message':"Choice Updated Successfully",
                    "Data":serializer.data
                },status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'error':serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            traceback.print_exc()
            return Response({
                "Error Message": "Something went wrong",
                "Error":str(e)
            },status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, *args, **kwargs):
        data = request.data
        choice_id = data.get('id')

        if not choice_id:
            return Response("Choice ID is required to delete object")
        try:
            choice_obj = Choice.objects.get(id = choice_id)
            choice_obj.delete()
            return Response(f"Choice with {choice_id} ID deleted ...")
        except Exception as e:
            traceback.print_exc()
            return Response({
                "Error Message": "Something went wrong",
                "Error":str(e)
            },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
