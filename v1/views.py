from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filterset_fields = ['price', 'category_name']
    search_fields = ['name', 'description']


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class ContactAPI(APIView):
    def post(self, request):
        serializers = ContactSerializers(data=request.data)
        if serializers.is_valid():
            data = serializers.validated_data
            send_mail(
                subject=f"Sizga habar keldi {data['name']} dan!",
                message=data['message'],
                from_email=data['email'],
                recipient_list=['nimadrcomapniyt@gmail.com']
            )
            return Response({'message': "Email mubofaqiyatli yuborildi !"}, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)




