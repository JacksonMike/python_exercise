from django.shortcuts import render, HttpResponse
from first.models import UserInfo
from AjaxDemo import settings
import json
import os


# Create your views here.
def index(request):
    return render(request, "index.html")


def deal_ajax(request):
    return HttpResponse("登陆成功")


def calculate(request):
    return render(request, "calculate.html")


def deal_calculate(request):
    """
    Django解析：
         if contentType："urlencoded":

               request.POST=data
         else:
               request.POST={}

    :param request:
    :return:
    """
    c1 = request.POST.get("c1")
    c2 = request.POST.get("c2")
    c3 = int(c1) + int(c2)
    # application/x-www-form-urlencoded; charset=UTF-8
    # 'c1=9&c2=9&csrfmiddlewaretoken=blNxtX6F5CXM41U8bz41RxrJYYi9JwcLoyuXWuL6eMFgFXibe66jWYUt7VDPhSmg'
    # print(request.body)
    print("*" * 1000)
    # <QueryDict: {'csrfmiddlewaretoken': ['7JivyPYLGSejpRUSgW2uFcoIZ2AwsQJ6kWZV1mDcP2WN0NiVjt4MKDRs8ZVc0cTB'], 'c2': ['8'], 'c1': ['8']}>
    # print(request.POST)
    return HttpResponse(str(c3))


def enter(request):
    res = {"user": None, "error": ""}
    if request.method == "GET":
        return render(request, "enter.html")
    else:
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        if UserInfo.objects.filter(user=user, pwd=pwd).first():
            res["user"] = user
        else:
            res["error"] = "用户名或者密码错误"
        # 返回json数据
        return HttpResponse(json.dumps(res))


def json_calculate(request):
    return render(request, "json_calculate.html")


def deal_json_calculate(request):
    json_dict = json.loads(request.body.decode("utf8"))
    # {'c2': '9', 'c1': '9'}
    c3 = int(json_dict["c2"]) + int(json_dict["c1"])
    return HttpResponse(str(c3))


def file_upload(request):
    return render(request, "file_upload.html")


def deal_file_upload(request):
    # <MultiValueDict: {'file_obj': [<InMemoryUploadedFile: 王道训练营（for JAVA方向）开营前需掌握的编程基础知识.pdf (application/pdf)>]}>
    print(request.FILES)
    # <QueryDict: {'user': ['Jim']}>
    print(request.POST)
    file_obj = request.FILES.get("file_obj")
    path_t = file_obj.name
    path = os.path.join(settings.BASE_DIR, "media", "img", path_t)
    with open(path, "wb") as f:
        for line in file_obj:
            f.write(line)
    return HttpResponse("OK")


def form_upload(request):
    return render(request, "form_upload.html")


def deal_form_upload(request):
    file_obj = request.FILES.get("file_obj")
    path_t = file_obj.name
    path = os.path.join(settings.BASE_DIR, "media", "img", path_t)
    with open(path, "wb") as f:
        for line in file_obj:
            f.write(line)
    return HttpResponse("上传成功")
