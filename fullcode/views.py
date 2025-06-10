from django.shortcuts import render
from rest_framework import generics
from .models import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
import requests
import os

