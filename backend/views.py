# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import os

from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
from backend.models import Book, UploadFile
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


@require_http_methods(["GET"])
def show_upload_file(request):
    response = {}
    try:
        upload_files = UploadFile.objects.filter()
        file_list = json.loads(serializers.serialize("json", upload_files))
        for file in file_list:
            file['fields']['url'] = "/static/video/"+file['fields']['file_name']
        print file_list
        response['list'] = file_list
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def delete_upload_file(request):
    response = {}
    try:
        response['data'] = UploadFile.objects.filter(pk=request.GET.get('id'))[0].file_name
        UploadFile.objects.filter(pk=request.GET.get('id')).update(status=0)
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

# 上传文件方法
def upload_file(request):
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
    upload_file = UploadFile(file_name = my_file.name,file_type = "mp3",user_name="fengxin",status=1)
    upload_file.save()
    response['list'] = json.loads(serializers.serialize("json", UploadFile.objects.filter()))
    response['msg'] = 'success'
    response['error_num'] = 0
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

