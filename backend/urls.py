# -*- coding: utf-8 -*-
from django.conf.urls import url

from backend import views

urlpatterns = [
    url(r'add_book$', views.add_book, ),
    url(r'show_books$', views.show_books, ),
    url(r'show_upload_file', views.show_upload_file, ),
    url(r'delete_upload_file', views.delete_upload_file, ),
    url(r'uploadFile', views.upload_file, ),
    url(r'upload$', views.upload, ),]