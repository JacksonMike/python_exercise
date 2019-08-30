from django.shortcuts import render, HttpResponse
from first.models import BookInfo
from django.core.paginator import Paginator, EmptyPage
from first.page import Pagination


# Create your views here.
def index(request):
    """
    批量插入数据
    book_list = []
    for i in range(1, 101):
        book = BookInfo(title="book_%s" % i, price=i * i - i)
        book_list.append(book)
    BookInfo.objects.bulk_create(book_list)
    :param request:
    :return:
    """
    """
    分页器的使用
    book_list = BookInfo.objects.all()
    paginator = Paginator(book_list, 10)
    # 总共多少页数据
    print(paginator.num_pages)
    # 总的数据条数
    print(paginator.count)
    # 页数的范围
    print(paginator.page_range)
    # <class 'first.models.BookInfo'>
    page = paginator.page(7)
    for i in page:
        print(type(i))
    # 是否有下一页
    print(page.has_next())
    # 是否有前一页
    print(page.has_previous())
    # 下一页页数
    print(page.next_page_number())
    # 前一页页数
    print(page.previous_page_number())
    """
    book_list = BookInfo.objects.all()
    paginator = Paginator(book_list, 10)
    try:
        # 获取当前页数,默认为1
        current_page_num = request.GET.get("page", 1)
        # 获取当前页数对象
        current_page = paginator.page(current_page_num)
    except EmptyPage as e:
        # 如果没有相应的页数,则默认为1
        current_page_num = 1
        current_page = paginator.page(1)
    return render(request, "index.html",
                  {"current_page": current_page, "current_page_num": int(current_page_num), "paginator": paginator})


def index2(request):
    current_page_num = request.GET.get("page")
    book_all = BookInfo.objects.all()
    pagination = Pagination(current_page_num, book_all.count(), request)
    book_list = book_all[pagination.start: pagination.end]
    return render(request, "index2.html", locals())
