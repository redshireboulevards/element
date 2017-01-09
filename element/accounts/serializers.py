from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'email', 'first_name', 'last_name', 'date_joined',
            'instagram_handle', 'bithdate', 'last_login'
        )
        read_only_fields = ('id', 'date_joined', 'last_login')
