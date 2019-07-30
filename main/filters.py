import django_filters

from .models import GoogleResultModel
from django_filters import rest_framework as filters

class ResultFilter(filters.FilterSet):
    keywords = django_filters.CharFilter(field_name='keywords', lookup_expr='icontains', label='Keywords')
    date = django_filters.DateTimeFilter(field_name='date', lookup_expr='icontains')
    class Meta:
        model = GoogleResultModel
        fields = ['keywords', 'link', 'date']


