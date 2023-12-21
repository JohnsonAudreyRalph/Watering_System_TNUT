# middleware.py
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

class CustomNotFoundMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 404:
            # Xử lý lỗi 404 tại đây
            return render(request, '404.html')
        return response