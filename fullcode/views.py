from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
import requests
from rest_framework import status
import os

TELEGRAM_BOT_TOKEN = "7280372184:AAEEEIXI5zJTxynOOTqcdAZ_wcORPHEWamU"
TELEGRAM_CHAT_ID = -1002782734267

@method_decorator(csrf_exempt, name='dispatch')
class ProjectContactView(generics.ListCreateAPIView):  
    serializer_class = ContactSerializer
    queryset = ProjectContact.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            projectcontact = serializer.save()

            try:
                message = (
                    f"💬 *Новая заявка от заказчиков!*\n\n"
                    f"👤 *Имя* {projectcontact.name}\n"
                    f"📞 *Телефон* {projectcontact.phone_number}\n"
                    f"✍️ *Сообщение* {projectcontact.text}\n"
                )

                url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
                payload = {
                    "chat_id": TELEGRAM_CHAT_ID,
                    "text": message,
                    "parse_mode": "Markdown"
                }

                response = requests.post(url, json=payload)

                if response.status_code == 200:
                    print("✅ Сообщение успешно отправлено!")
                else:
                    print(f"⚠️ Ошибка при отправке сообщения. Ответ: {response.text}")

            except Exception as e:
                print(f"❌ Ошибка отправки сообщения в Telegram: {e}")
                return Response({"Ошибка": "Не удалось отправить сообщение в Telegram"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class ServicesView(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class ProjectView(generics.ListAPIView):
    queryset = Progect.objects.all()
    serializer_class = ProjectSerializer


class ComandsView(generics.ListAPIView):
    queryset = Comands.objects.all()
    serializer_class = ComandsSerializer


class SchoolContactView(generics.ListCreateAPIView):
    serializer_class = SchoolContactSerializer
    queryset = SchoolContact.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            schoolcontact = serializer.save()

            try:
                message = (
                    f"💬 *Новая заявка от учащихся!*\n\n"
                    f"👤 *Имя* {schoolcontact.name}\n"
                    f"📞 *Телефон* {schoolcontact.phone_number}\n"
                    f"✍️ *Сообщение* {schoolcontact.text}\n"
                )

                url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
                payload = {
                    "chat_id": TELEGRAM_CHAT_ID,
                    "text": message,
                    "parse_mode": "Markdown"
                }

                response = requests.post(url, json=payload)

                if response.status_code == 200:
                    print("✅ Сообщение успешно отправлено!")
                else:
                    print(f"⚠️ Ошибка при отправке сообщения. Ответ: {response.text}")

            except Exception as e:
                print(f"❌ Ошибка отправки сообщения в Telegram: {e}")
                return Response({"Ошибка": "Не удалось отправить сообщение в Telegram"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CoursesView(generics.ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer


class ProsView(generics.ListAPIView):
    queryset = Pros.objects.all()
    serializer_class = ProsSerializer


class CertificatesView(generics.ListAPIView):
    queryset = Certificates.objects.all()
    serializer_class = CertificatesSerializer