from rest_framework import serializers 
from .models import *

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectContact 
        fields = "__all__"

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progect
        fields = "__all__"

class ComandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comands
        fields = "__all__"

class SchoolContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolContact
        fields = "__all__"

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = "__all__"

class ProsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pros
        fields = "__all__"


class CertificatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificates
        fields = "__all__"

