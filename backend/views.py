# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import os

from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
from backend.models import Book
from django_jl.settings import UPLOAD_URL, BASE_DIR


@require_http_methods(["GET"])
def add_book(request):
    response = {}
    try:
        book = Book(book_name=request.GET.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_books(request):
    response = {}
    try:
        books = Book.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 上传文件方法
def upload(request):
    response = {}
    if request.method == "POST":
        my_file = request.FILES.get("file", None)
    if not my_file:
        response['msg'] = 'error'
        response['error_num'] = 1
        return JsonResponse(response)
    destination = open(os.path.join(BASE_DIR, UPLOAD_URL, my_file.name), 'wb+')
    for chunk in my_file.chunks():
        destination.write(chunk)
        destination.close()
    response['msg'] = 'success'
    response['error_num'] = 0
    response['file_url'] = '/static/video/'+my_file.name
    return JsonResponse(response)

