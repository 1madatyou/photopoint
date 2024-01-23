from rest_framework.serializers import ModelSerializer

from .models import CurrencyRate

class CurrencyRateSerializer(ModelSerializer):
    class Meta:
        model = CurrencyRate
        fields = '__all__'