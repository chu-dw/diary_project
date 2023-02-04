from django.contrib.auth.models import User
from django.contrib.auth.password_vaildation import validate_password

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

class RegisterSerailizer(serializers.ModelSerializer):
    email = serailizers.EmailField(
        required=True,
        valiators=[UniqueValidator(queryset=User.objects.all())],
    )

    password = serializers.CHarField(
        write_only=True,
        required=True,        
    )

    password2 = serializers.CHarField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("username", "password", )