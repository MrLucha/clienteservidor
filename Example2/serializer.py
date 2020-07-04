from rest_framework import routers,serializers,viewsets
from Example2.models import ExampleModel

class Example2Serializer(serializers.ModelSerializer):
    name=serializers.CharField(required=False)
    age=serializers.IntegerField(required=False)
    address=serializers.CharField(required=False)
    curp=serializers.CharField(required=False)
    class Meta: 
        model=ExampleModel
        fields=('__all__')