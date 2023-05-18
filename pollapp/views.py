from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from pollapp import response
from .models import pollvoters
import json as j
from rest_framework import viewsets
from .serializer import PollSerializer

class poll(viewsets.ModelViewSet):  #generics.ListCreateAPIView for general get methods or default methods
    def get(self, request):
        model_object = pollvoters.objects.all()  
        serializers = PollSerializer(model_object, many=True).data
        # Response_data = {

        # }
        return response.Response(serializers, True)
    def post(self, request):
        request_data = j.loads(request.body.decode('utf-8'))
        model_object = pollvoters()
        model_object.first_name = request_data['first_name']
        model_object.last_name = request_data['last_name']
        model_object.address = request_data['address']
        model_object.Location = request_data['location']
        model_object.save()
        return response.Response("post is success", True)
# class userviews(viewssets.ModelViewSet):
#      def get(self, request)
#         var = User.objects.all()
#         serializer = UserSerializer(var, many=True).data
    def put(self, request, id):        
        request_data = j.loads(request.body.decode('utf-8'))
        pollvoters.objects.filter(id=id).update(
            address=request_data['address'], 
            first_name = request_data['first_name'], 
            last_name = request_data['last_name'],
            restaurant = request_data['restaurant'],
            Location = request_data['location'])
        return response.Response("put is success", True)