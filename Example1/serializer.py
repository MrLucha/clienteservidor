from rest_framework import routers,serializers,viewsets
from Example1.models import ExampleModel

class Example1Serializer(serializers.ModelSerializer):
    class Meta:
        model=ExampleModel
        fields=('__all__')