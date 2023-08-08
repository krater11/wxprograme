from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django_redis import get_redis_connection
from utils.randomcode.randomcode import RandomCode
from Serializers.MessageSerializer import MessageSerializer
from Serializers.LoginSerializer import LoginSerializer
from WxPrograme import models
import uuid


class MessageView(APIView):
    def get(self, request, *args, **kwargs):
        phone = request.query_params.get('phone')
        print(phone)

        ser = MessageSerializer(data=request.query_params)
        if not ser.is_valid():
            return Response({'status': False, 'message': '手机格式错误'})
            print(ser.validated_data)

        phone = ser.validated_data.get('phone')
        random_code = RandomCode()

        #tencent.send_message(phone,random_code)
        conn = get_redis_connection()
        conn.set(phone, random_code, ex=60)

        return Response({'status': True, 'message': '发送成功'})


class LoginView(APIView):

    def post(self, request, *args, **kwargs):
        print(request.data)
        ser = LoginSerializer(data=request.data)
        if not ser.is_valid():
            return Response({'status': False, 'message': '验证码错误'})

        phone = ser.validated_data.get('phone')

        user_object, flag = models.UserInfo.objects.get_or_create(phone=phone)
        user_object.token = str(uuid.uuid4())
        user_object.save()

        return Response({'status': True, 'data': {'token': user_object.token, 'phone': phone}})

    def login(self, request, *args, **kwargs):
        print(request.data)
        return Response({'status': True})