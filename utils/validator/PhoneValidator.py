import re
from rest_framework.exceptions import ValidationError


def phone_validator(value):
    if not re.match(r'^(13[0-9]|14[0|5|6|7|9]|15[0|1|2|3|5|6|7|8|9]|'
                         r'16[2|5|6|7]|17[0|1|2|3|5|6|7|8]|18[0-9]|'
                         r'19[1|3|5|6|7|8|9])\d{8}$',value):
        raise ValidationError('手机格式错误')