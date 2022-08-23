from django_filters import rest_framework as filters

from src.producer.models import Producer


class ProducerFilter(filters.FilterSet):
    class Meta:
        model = Producer
        fields = {"name": ["iexact"], "email": ["iexact"]}
