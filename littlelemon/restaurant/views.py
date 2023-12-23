from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from .models import Menu, Booking
from . import serializers

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = serializers.UserSerializer
   permission_classes = [permissions.IsAuthenticated] 

class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = serializers.MenuSerializer 

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = serializers.MenuSerializer  

class BookingViewSet(viewsets.ModelViewSet):
   queryset = Booking.objects.all()
   serializer_class = serializers.BookingSerializer
   permission_classes = [permissions.IsAuthenticated] 
