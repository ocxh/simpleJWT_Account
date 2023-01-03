from rest_framework import serializers
from .models import Account
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Account.objects.all())],
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Account
        fields = ('nickname', 'password', 'password2', 'email')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return data

    def create(self, validated_data):
        user = Account.objects.create_user(
            nickname=validated_data['nickname'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        
        user.save()
        return user
    
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(
        required = True,
        write_only = True
    )
    password = serializers.CharField(
        required = True,
        write_only = True,
    )
    class Meta(object):
        model = Account
        fields = ('email', 'password')

    def validate(self, data):
        email = data.get('email',None)
        password = data.get('password',None)

        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email=email)

            if not user.check_password(password):
                raise serializers.ValidationError('Check Your Email or Password')
        
        else:
            raise serializers.ValidationError("User does not exist")
        

        token = RefreshToken.for_user(user=user)
        data = {
            'refresh_token' : str(token),
            'access_token' : str(token.access_token)
        }
        return data