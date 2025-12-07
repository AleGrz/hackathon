import json

from django.http import JsonResponse
from django.shortcuts import render
from core.model import get_result

def index(request):
    return render(request, "index.html")

def generate(request):
    return JsonResponse(get_result(json.loads(request.body)["data"]))