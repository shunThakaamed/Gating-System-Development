# your-repo/src/authentication/serializers.py

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'wallet_address']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            wallet_address=validated_data['wallet_address']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
