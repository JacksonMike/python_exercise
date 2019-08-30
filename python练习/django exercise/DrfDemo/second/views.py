from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin

from first.models import Book
from second.serializers import BookSerializer
from utils.pagination import MyPaginator, YourPaginator, OurPaginator
from rest_framework import views, viewsets, generics, mixins


class GenericAPIView(APIView):
    queryset = None
    serializer_class = None

    def get_queryset(self):
        return self.queryset.all()

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)


class ListModelMixin(object):
    """展示图书"""

    def list(self, request):
        queryset = self.get_queryset()
        ser_obj = self.get_serializer(queryset, many=True)
        return Response(ser_obj.data)


class CreateModelMixin(object):
    """添加图书"""

    def create(self, request):
        ser_obj = self.get_serializer(data=request.data)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(ser_obj.data)
        else:
            return Response(ser_obj.errors)


class RetrieveModelMixin(object):
    def retrieve(self, request, id):
        book_obj = self.get_queryset().filter(id=id).first()
        ser_obj = BookSerializer(book_obj)
        return Response(ser_obj.data)


class UpdateModelMixin(object):
    """编辑书籍"""

    def update(self, request, id):
        book_obj = self.get_queryset().filter(id=id).first()
        ser_obj = self.get_serializer(instance=book_obj, data=request.data, partial=True)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(ser_obj.data)
        else:
            return Response(ser_obj.errors)


class DestroyModelMixin(object):
    """删除书籍"""

    def destroy(self, request, id):
        book_obj = self.get_queryset().filter(id=id).first()
        if not book_obj:
            return Response("删除的对象不存在")
        book_obj.delete()
        return Response("")


class ListCreateAPIView(GenericAPIView, ListModelMixin, CreateModelMixin):
    pass


class RetrieveUpdateDestroyAPIView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    pass


class ModelViewSet(ViewSetMixin, ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    pass


class BookView(ListCreateAPIView):
    """书籍展示"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        """书籍添加"""
        return self.create(request)


class BookEditView(RetrieveUpdateDestroyAPIView):
    """书籍展示"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, id):
        return self.retrieve(request, id)

    """书籍修改"""

    def put(self, request, id):
        return self.update(request, id)

    """书籍删除"""

    def delete(self, request, id):
        return self.destroy(request, id)


class BookModelView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = OurPaginator


class PageView(APIView):
    def get(self, request):
        book_list = Book.objects.all()
        # 分页
        # page_obj = MyPaginator()
        # page_obj = YourPaginator()
        page_obj = OurPaginator()
        page_article = page_obj.paginate_queryset(queryset=book_list, request=request, view=self)
        ret = BookSerializer(page_article, many=True)
        return page_obj.get_paginated_response(ret.data)

# YourPaginator http://127.0.0.1:8000/book?offset=2&limit=1  在第n个位置  向后查看n条数据
# MyPaginator http://127.0.0.1:8000/book?page=2&size=1
