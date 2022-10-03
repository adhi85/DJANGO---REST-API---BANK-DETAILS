from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import Bank
from .serializers import BankSerializer,Full
from base.api import serializers


@api_view(['GET'])
def Routes(request):
    routes = [
        'VIEW ALL COMMANDS: GET /api',
        'VIEW ALL BANK LIST: GET/api/banks',
        'BRANCH DETAILS FOR SPECIFIC BRANCH: GET/api/banks/ifsc',
    ]

    return Response(routes)

@api_view(['GET'])
def getbankList(request):
    banks = Bank.objects.all()
    serializer = BankSerializer(banks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBank(request, pk):
    bank = Bank.objects.get(ifsc = pk)
    serializer = Full(bank, many=False)
    return Response(serializer.data)