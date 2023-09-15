from django.shortcuts import render
from rest_framework.generics import *
from .models import *
from .serializers import *

# Create your views here.

class studentlist(ListAPIView):
    queryset=student1.objects.all()
    serializer_class=studentserializer1

class studentcreate(CreateAPIView):
    queryset=student1.objects.all()
    serializer_class=studentserializer1  
    
      
class studentretrive(RetrieveAPIView):
    queryset=student1.objects.all()
    serializer_class=studentserializer1 
    
class studentupdate(UpdateAPIView):
    queryset=student1.objects.all()
    serializer_class=studentserializer1 
    
class studentdelete(DestroyAPIView):
    queryset=student1.objects.all()
    serializer_class=studentserializer1  
    
class studentlistcreate(ListCreateAPIView):
    queryset=student1.objects.all()
    serializer_class=studentserializer1            