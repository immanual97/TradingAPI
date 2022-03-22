from rest_framework import serializers
from tradingapp.models import Trade

class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trade
        fields=('date','open','high','low','close','adjclose','volume')