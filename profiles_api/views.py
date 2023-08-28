from rest_framework.views import APIView #imports APIView class from the rest_framework.views module
from rest_framework.response import Response #imports the response framework which is used to return responses from the API view


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None): #retrieves a list of objects
        """Returns a list of APIView features"""
        an_apiview = [
            'User HTTP methods as function (get, post, patch, put, delete)'
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
