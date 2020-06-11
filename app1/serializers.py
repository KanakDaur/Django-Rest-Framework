from rest_framework import serializers
from .models import Product



# code to convert all the dictionary items into JSON format (serialization)
class productserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
