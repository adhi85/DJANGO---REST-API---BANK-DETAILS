from dataclasses import field
from rest_framework.serializers import ModelSerializer
from base.models import Bank

class BankSerializer(ModelSerializer):
    class Meta:
        model = Bank
        fields = ['ifsc','branch' ,'bank_name']

class Full(ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'