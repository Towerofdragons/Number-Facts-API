from django.shortcuts import render
from rest_framework import permissions, authentication, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

from .service import FetchNumberAPI
from .serializer import APIFailSerializer, APISuccessSerializer
from . import utils
# Create your views here.

"""
GET** <your-url>/api/classify-number?number=371
"""
class get_fact(APIView):
  """
  Recieve get request and request Numbers api using response data
  """
  renderer_classes = [JSONRenderer]
  def get(self, request):
    number = request.query_params.get("number", None)
    print(number)

    try:
      number = int(number)
    except Exception as e:
      data = {"number": number,
              "error": True}
      
      return Response(data, status=status.HTTP_400_BAD_REQUEST)
    
    try:
      response = FetchNumberAPI(number)
      text = response.get("text")
      print(response)
    except Exception:
      Response({"Error": "something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    
    data = {
            "number" : number,
            "is_prime" : utils.is_prime(number),
            "is_perfect" : utils.is_perfect(number),
            "properties" : [].append(utils.is_armstrong(number)),
            "digit_sum" : utils.digit_sum(number),
            "fun_fact" : text
            }

    return Response(data, status=status.HTTP_200_OK)