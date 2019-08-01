from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import GoogleResultModel
from main.api.serializers import ResultSerachSerializer
from rest_framework import generics, filters

class ResultSearchList(generics.ListAPIView):
    """
    Return a list of all the products that the authenticated
    user has ever purchased, with optional filtering.
    """
    queryset = GoogleResultModel.objects.all()
    serializer_class = ResultSerachSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['keywords', 'date', 'link']

