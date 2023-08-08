from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import re
from rest_framework import serializers
import re
from rest_framework.exceptions import ValidationError
import random
from django_redis import get_redis_connection
from utils.randomcode.randomcode import RandomCode

def phone_validator(value):
    if not re.match(r'^(13[0-9]|14[0|5|6|7|9]|15[0|1|2|3|5|6|7|8|9]|'
                         r'16[2|5|6|7]|17[0|1|2|3|5|6|7|8]|18[0-9]|'
                         r'19[1|3|5|6|7|8|9])\d{8}$',value):
        raise ValidationError('手机格式错误')


class MessageSerializer(serializers.Serializer):
    phone = serializers.CharField(label='手机号',validators=[phone_validator,])


class LoginView(APIView):

    def login(self,request,*args,**kwargs):
        print(request.data)
        return Response({'status':True})


class MessageView(APIView):
    def get(self,request,*args,**kwargs):
        phone = request.query_params.get('phone')
        print(phone)

        ser = MessageSerializer(data=request.query_params)
        if not ser.is_valid():
            return Response({'status':False,'message':'手机格式错误'})
            print(ser.validated_data)

        phone = ser.validated_data.get('phone')
        random_code = RandomCode()

        #tencent.send_message(phone,random_code)
        conn = get_redis_connection()
        conn.set(phone,random_code,ex=30)

        return Response({'status':True,'message':'发送成功'})