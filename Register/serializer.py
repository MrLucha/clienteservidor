from rest_framework import routers, serializers,viewsets 
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields = ('username','password','email')

    def create(self, validated_data):
       
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            is_superuser=True,
        )
        user.set_password(validated_data['password'])
        user.save()
        return user