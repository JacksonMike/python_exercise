from rest_framework import pagination


class MyPaginator(pagination.PageNumberPagination):
    # http://127.0.0.1:8000/book?page=2&size=1
    page_size = 2
    page_query_param = 'page'
    page_size_query_param = 'size'
    max_page_size = 3


class YourPaginator(pagination.LimitOffsetPagination):
    default_limit = 1
    limit_query_param = 'limit'
    offset_query_param = 'offset'


class OurPaginator(pagination.CursorPagination):
    cursor_query_param = 'cursor'
    # 排序字段
    ordering = 'id'
    page_size = 2
