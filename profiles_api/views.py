from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from  profiles_api import serializers
from rest_framework import viewsets
from  profiles_api import permissions
from  profiles_api import models
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

class HelloApiView(APIView):
    """ Test API View """
    serializer_class = serializers.HelloSerializer

    def get(self, request , format = None):
      """ Returns a list of APIView features"""

      an_apiview = [
          'uses HTTP methods as function ( get, post , put , patch , delete)',
          'Is similar to the traditional Django view' ,
          'Gives you the most control over your application logic' ,
          'Is mapped manually to URLs',
      ]

      return Response({ 'message' : 'Hello!' , 'an_apiview' : an_apiview})

    def post(self , request):
        """ create a hello message with our name """
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'Hello {}'.format(name)
            return Response({'message' : message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self , request , pk=None):
        """ Handle updating an object"""
        return Response({'method': 'PUT'})



    def patch(self, request, pk=None):
        """ Handle partial updating an object"""
        return Response({'method': 'PATCH'})


    def delete(self, request, pk=None):
        """ Handle deleting an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ Test API Viewset """
    serializer_class = serializers.HelloSerializer

    def list(self , request):
        """ Return a hello message """

        a_viewset =  [
            'Uses actions ( list , create , retreive , update , partial_update)',
            'Automatically maps to URLs using routers' ,
            'provides more functionality with less code',
        ]
        return Response({ 'message' : 'Hello!' , 'a_viewset' : a_viewset })


    def create(self, request):
        """ creates a new hello message """

        serializer = self.serializer_class(data= request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message='Hello {}!'.format(name)
            return Response({ 'message' : message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


    def retrieve(self , request , pk=None):
        """ Handle getting an object by it's ID"""

        return Response({'http_method' : 'GET'})

    def update(self, request, pk=None):
        """ Handle updating an object by it's ID"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """ Handle partially updating an object by it's ID"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """ Handle pdeleting an object by it's ID"""

        return Response({'http_method': 'DELETE'})

class  UserProfileViewSet(viewsets.ModelViewSet):
    """ Handles creating and updating profiles """

    serializer_class = serializers.UserProfileSerializer
    queryset =  models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name' , 'email' ,)