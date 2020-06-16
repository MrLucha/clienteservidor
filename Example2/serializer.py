from rest_framework import routers,serializers,viewsets
from Example2.models import ExampleModel

class Example2Serializer(serializers.ModelSerializer):
    class Meta:
        model=ExampleModel
        fields=('__all__')