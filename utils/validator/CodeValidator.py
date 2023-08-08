import re
from rest_framework.exceptions import ValidationError
from django_redis import get_redis_connection


def code_validator(self, value):
    if len(value) != 6:
        raise ValidationError('短信格式错误')
    if not value.isdecimal():
        raise ValidationError('短信格式错误')

    phone = self.initial_data.get('phone')
    conn = get_redis_connection()
    conn.get()
    code = conn.get(phone)
    if not code:
        raise ValidationError('验证码过期')
    if value != code.decode('utf-8'):
        raise ValidationError('验证码错误')

    return value
