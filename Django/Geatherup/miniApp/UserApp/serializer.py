from rest_framework import serializers
# from rest_framework.serializers import ModelSerializer
from UserApp.models import User

class Userserializer(serializers.ModelSerializer):
    password = serializers.CharField(source='password', write_only=True)
    class Meta:
        model = User
        fields = '__all__'