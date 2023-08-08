from rest_framework import serializers
from utils.validator.PhoneValidator import phone_validator


class MessageSerializer(serializers.Serializer):
    phone = serializers.CharField(label='手机号',validators=[phone_validator,])