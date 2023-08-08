from rest_framework import serializers
from utils.validator.PhoneValidator import phone_validator
from utils.validator.CodeValidator import code_validator


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(label='手机号', validators=[phone_validator, ])
    code = serializers.CharField(label='验证码', validators=[code_validator, ])

