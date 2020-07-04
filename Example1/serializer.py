from rest_framework import routers,serializers,viewsets
from Example1.models import ExampleModel

class Example1Serializer(serializers.ModelSerializer):
    name=serializers.CharField(required=False)
    age=serializers.IntegerField(required=False)
    address=serializers.CharField(required=False)
    curp=serializers.CharField(required=False)
    class Meta:
        model=ExampleModel
        fields=('__all__')

# class AdminSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(required=True)
#     class Meta:
#         model=User
#         model.is_superuser=True
#         #fields = ['id','username', 'email']
#         fields=('__all__')
