from django.shortcuts import render
from django.http.response import JsonResponse

from tradingapp.models import Trade
from tradingapp.serializer import TradeSerializer

# Create your views here.

def GetAllRecordbyDateApi(request,date=""):
    if request.method=='GET':
        trade=Trade.objects.filter(date=date)
        #trade=Trade.objects.all()
        trade_serializer=TradeSerializer(trade,many=True)
        return JsonResponse(trade_serializer.data,safe=False)