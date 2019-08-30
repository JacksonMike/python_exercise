from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.views import View
from django.core import serializers
from .models import Book


class BookView(View):
    def get(self, request):
        print(type(request))
        book_queryset = Book.objects.all()
        data = serializers.serialize("json", book_queryset, ensure_ascii=False)
        return HttpResponse(data)
