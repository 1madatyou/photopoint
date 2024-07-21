from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from .models import CurrencyRate
from .serializers import CurrencyRateSerializer


class USDRUBView(APIView):

    def get(self, request):

        try:
            rates = CurrencyRate.objects.filter(
                from_currency="USD",
                to_currency="RUB",
            ).order_by("-id")[:10]
        except CurrencyRate.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

        serializer = CurrencyRateSerializer(rates, many=True)

        return Response(data=serializer.data, status=HTTP_200_OK)
