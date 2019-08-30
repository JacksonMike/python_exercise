from django.shortcuts import render, HttpResponse, redirect
from django.forms.models import modelformset_factory
from first.form import UserForm, ConsultRecordModelForm
from django.contrib.auth.decorators import login_required
from PIL import Image, ImageDraw, ImageFont
from first.form import CustomerModelForm, StudentStudyRecordModelForm
from first.utils.page import Pagination
from django.http import JsonResponse
from django.db.models import Q, Count
from django.contrib import auth
from django.urls import reverse
from django.views import View
from first.models import *
from io import BytesIO
import datetime
import random


# Create your views here.
def enter_required(func):
    """自定义登陆装饰器"""

    def inner(request):
        if not request.user.id:
            return redirect("/enter/")
        else:
            ret = func(request)
            return ret

    return inner


def enter(request):
    """登陆功能"""
    if request.method == "GET":
        return render(request, "enter.html")
    else:
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        code = request.POST.get("code")
        response = {"user": None, "error_message": ""}
        if code.upper() == request.session.get("keep_str").upper():
            user_obj = auth.authenticate(username=user, password=pwd)
            if user_obj:
                auth.login(request, user_obj)
                response["user"] = user
            else:
                response["error_message"] = "用户名或者密码错误"
        else:
            response["error_message"] = "验证码错误"
        return JsonResponse(response)


def leave(request):
    auth.logout(request)
    return redirect("/enter/")


def get_color():
    """获取随机颜色"""
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def get_img(request):
    """获取验证码功能"""
    # 第一种方式
    # with open("static/img/a.jpg", "rb") as f:
    #     data = f.read()
    # return HttpResponse(data)

    # 第二种
    # img = Image.new("RGB", (350, 38), (get_color()))
    # f = open("static/img/b.png", "wb")
    # img.save(f, "png")
    # with open("static/img/b.png", "rb") as f:
    #     data = f.read()
    # return HttpResponse(data)

    # 第三种
    # img = Image.new("RGB", (350, 38), (get_color()))
    # f = BytesIO()
    # img.save(f, "png")
    # data = f.getvalue()
    # return HttpResponse(data)

    # 第四种
    # img = Image.new("RGB", (350, 38), (get_color()))
    # draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype("static/font/kumo.ttf", 32)
    # draw.text((0, 0), "python!", (get_color()), font=font)
    # f = BytesIO()
    # img.save(f,"png")
    # data=f.getvalue()
    # return HttpResponse(data)

    # 第五种 绘制验证码
    img = Image.new("RGB", (350, 38), (get_color()))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("static/font/kumo.ttf", 32)
    keep_str = ""
    for i in range(6):
        random_num = str(random.randint(0, 9))
        random_low = chr(random.randint(97, 122))
        random_upper = chr(random.randint(65, 90))
        random_char = random.choice([random_num, random_low, random_upper])
        draw.text((i * 30 + 50, 0), random_char, (get_color()), font=font)
        keep_str += random_char
    f = BytesIO()
    img.save(f, "png")
    data = f.getvalue()
    request.session["keep_str"] = keep_str
    print('keep_str', keep_str)
    return HttpResponse(data)


def register(request):
    """注册功能"""
    if request.method == "GET":
        form = UserForm()
        return render(request, "register.html", locals())
    else:
        form = UserForm(request.POST)
        response = {"user": None, "error_message": ""}
        if form.is_valid():
            response["user"] = request.POST.get("user")
            print(form.cleaned_data)
            user = form.cleaned_data.get("user")
            pwd = form.cleaned_data.get("pwd")
            email = form.cleaned_data.get("email")
            UserInfo.objects.create_user(username=user, password=pwd, email=email)
        else:
            print(form.errors)
            response["error_message"] = form.errors
        return JsonResponse(response)


# @enter_required
@login_required
def index(request):
    """首页"""
    return render(request, "index.html")


# @enter_required
# @login_required
# http://127.0.0.1:8000/enter/?next=/customers_list/
# def customers_list(request):
#     if reverse("customers_list") == request.path:
#         customer = Customer.objects.all()
#     else:
#         customer = Customer.objects.filter(consultant=request.user)
#     # search搜索
#     val = request.GET.get("q")
#     field = request.GET.get("field")
#     if val:
#         q = Q()
#         q.children.append((field+"__contains", val))
#         customer = Customer.objects.filter(q)
#     # 分页
#     current_page_num = request.GET.get("page")
#     pagination = Pagination(current_page_num, customer.count(), request)
#     customer = customer[pagination.start:pagination.end]
#     return render(request, "customers_list.html", locals())

class CustomerView(View):
    def get(self, request):
        if reverse("customers_public") == request.path:
            label = "公户列表"
            customer = Customer.objects.filter(consultant__isnull=True)
        elif reverse("customers_list") == request.path:
            label = "全部客户"
            customer = Customer.objects.all()
        else:
            label = "私户列表"
            customer = Customer.objects.filter(consultant=request.user)
        # search搜索
        val = request.GET.get("q")
        field = request.GET.get("field")
        if val:
            q = Q()
            q.children.append((field + "__contains", val))
            customer = Customer.objects.filter(q)
        # 分页
        current_page_num = request.GET.get("page")
        pagination = Pagination(current_page_num, customer.count(), request)
        customer = customer[pagination.start:pagination.end]

        path = request.path
        next_path = "?next=%s" % path
        print(path)
        print(next_path)

        return render(request, "customer/customers_list.html", locals())

    def post(self, request):
        print(request.POST)
        func_str = request.POST.get("action")
        data = request.POST.getlist("selected_pk_list")
        if not hasattr(self, func_str):
            return HttpResponse("操作错误")
        else:
            func = getattr(self, func_str)
            queryset = Customer.objects.filter(pk__in=data)
            ret = func(request, queryset)
            if ret:
                return ret
            return redirect(request.path)

    def batch_delete(self, request, queryset):
        queryset.delete()

    def batch_reverse_private(self, request, queryset):
        ret = queryset.filter(consultant__isnull=True)
        if ret:
            ret.update(consultant=request.user)
        else:
            return HttpResponse("手速太慢了")

    def batch_reverse_public(self, request, queryset):
        queryset.update(consultant=None)


# class CustomerAddView(View):
#     def get(self, request):
#         cmf = CustomerModelForm()
#         return render(request, "customers_add.html", locals())
#
#     def post(self, request):
#         cmf = CustomerModelForm(request.POST)
#         if cmf.is_valid():
#             cmf.save()
#             return redirect(reverse("customers_list"))
#         else:
#             return render(request, "customers_add.html", locals())
#
#
# class CustomerEditView(View):
#     def get(self, request, id1):
#         edit_obj = Customer.objects.get(pk=id1)
#         cmf = CustomerModelForm(instance=edit_obj)
#         return render(request, "customers_edit.html", locals())
#
#     def post(self, request, id1):
#         edit_obj = Customer.objects.get(pk=id1)
#         cmf = CustomerModelForm(request.POST, instance=edit_obj)
#         if cmf.is_valid():
#             cmf.save()
#             return redirect(request.GET.get("next"))
#         else:
#             return render(request, "customers_edit.html", locals())


class ConsultRecordView(View):
    def get(self, request):
        cr = ConsultRecord.objects.filter(consultant=request.user)
        customer_id = request.GET.get("customer_id")
        if customer_id:
            cr = ConsultRecord.objects.filter(customer_id=customer_id)
        return render(request, "customer/consult_records.html", locals())


class CustomerViewAddEdit(View):
    def get(self, request, edit_id=None):
        edit_obj = Customer.objects.filter(pk=edit_id).first()
        cmf = CustomerModelForm(instance=edit_obj)
        return render(request, "customer/customers_add_edit.html", locals())

    def post(self, request, edit_id=None):
        edit_obj = Customer.objects.filter(pk=edit_id).first()
        cmf = CustomerModelForm(request.POST, instance=edit_obj)
        if cmf.is_valid():
            cmf.save()
            return redirect(request.GET.get("next"))
        else:
            return render(request, "customer/customers_add_edit.html", locals())


class ConsultRecordAddEdit(View):
    def get(self, request, edit_id=None):
        edit_obj = ConsultRecord.objects.filter(pk=edit_id).first()
        crmf = ConsultRecordModelForm(instance=edit_obj)
        return render(request, "customer/consult_record_add_edit.html", locals())

    def post(self, request, edit_id=None):
        edit_obj = ConsultRecord.objects.filter(pk=edit_id).first()
        crmf = ConsultRecordModelForm(request.POST, instance=edit_obj)
        if crmf.is_valid():
            crmf.save()
            return redirect(reverse('consult_records'))
        else:
            return render(request, "customer/consult_record_add_edit.html", locals())


class ClassStudyRecordView(View):
    def get(self, request):
        class_study_record_list = ClassStudyRecord.objects.all()
        return render(request, "student/class_study_record.html", locals())

    def post(self, request):
        # <QueryDict: {'selected_pk_list': ['4'], 'action': ['batch_init'], 'csrfmiddlewaretoken': ['LmdY4rMOYZk7VtU4yPo0DJppHeDBof7DFJmYfFrT5btzf5fuIsYKfMIG1wUZUvXZ']}>
        print(request.POST)
        action = request.POST.get("action")
        selected_pk_list = request.POST.getlist("selected_pk_list")
        if hasattr(self, action):
            ret = getattr(self, action)(selected_pk_list)
        return self.get(request)

    def batch_init(self, selected_pk_list):
        for class_study_record_pk in selected_pk_list:
            # 获取班级信息
            class_study_record_obj = ClassStudyRecord.objects.filter(pk=class_study_record_pk).first()
            # 获取学生信息
            student_list = class_study_record_obj.class_obj.students.all()
            print(student_list)
            for student in student_list:
                StudentStudyRecord.objects.create(student=student, class_study_record=class_study_record_obj)


# class RecordScoreView2(View):
#     def get(self, request, class_study_record_id):
#         class_study_record_obj = ClassStudyRecord.objects.get(id=class_study_record_id)
#         student_study_record_list = class_study_record_obj.studentstudyrecord_set.all()
#         scs = StudentStudyRecord.score_choices
#         return render(request, "student/record_score.html", locals())
#
#     def post(self, request, class_study_record_id):
#         print(request.POST)
#         # {'7': {'score': '60', 'homework_note': '我是中国人 '}}
#         data_dict = {}
#         for key, val in request.POST.items():
#             if key == "csrfmiddlewaretoken":
#                 continue
#             field, pk = key.rsplit("_", 1)
#             if pk not in data_dict:
#                 data_dict[pk] = {
#                     field: val
#                 }
#             else:
#                 data_dict[pk][field] = val
#         print(data_dict)
#         for pk, data in data_dict.items():
#             StudentStudyRecord.objects.filter(pk=pk).update(**data)
#         return redirect(request.path)


class RecordScoreView(View):
    def get(self, request, class_study_record_id):
        model_formset_cls = modelformset_factory(model=StudentStudyRecord, form=StudentStudyRecordModelForm, extra=0)
        queryset = StudentStudyRecord.objects.filter(class_study_record=class_study_record_id)
        formset = model_formset_cls(queryset=queryset)
        return render(request, "student/record_score.html", locals())

    def post(self, request, class_study_record_id):
        print("request.POST", request.POST)
        model_formset_cls = modelformset_factory(model=StudentStudyRecord, form=StudentStudyRecordModelForm, extra=0)
        queryset = StudentStudyRecord.objects.filter(class_study_record=class_study_record_id)
        formset = model_formset_cls(request.POST)
        if formset.is_valid():
            formset.save()
        print("formset.errors", formset.errors)
        return redirect(request.path)


class StatisticsView(View):
    def today(self):
        today = datetime.datetime.now().date()
        customer_list = Customer.objects.filter(deal_date=today)
        # 查询每一个销售的名字已经今天对应的成单量
        ret = UserInfo.objects.filter(depart_id=1, customers__deal_date=today).annotate(
            c=Count("customers")).values_list("username", "c")
        ret = [[item[0], item[1]] for item in list(ret)]
        return {"customer_list": customer_list, "ret": list(ret)}

    def yesterday(self):
        import datetime
        yesterday = datetime.datetime.now().date() - datetime.timedelta(days=1)
        customer_list = Customer.objects.filter(deal_date=yesterday)
        # 查询每一个销售的名字以及昨天对应的成单量
        ret = UserInfo.objects.filter(depart_id=1, customers__deal_date=yesterday).annotate(
          c=Count("customers")).values_list("username", "c")

        ret = [[item[0], item[1]] for item in list(ret)]
        return {"customer_list": customer_list, "ret": list(ret)}

    def week(self):
        today = datetime.datetime.now().date()
        one_week = datetime.datetime.now().date()-datetime.timedelta(weeks=1)
        customer_list = Customer.objects.filter(deal_date__gte=one_week,deal_date__lte=today)
        ret = UserInfo.objects.filter(depart_id=1, customers__deal_date__gte=one_week,customers__deal_date__lte=today).annotate(
            c=Count("customers")).values_list("username", "c")

        ret = [[item[0], item[1]] for item in list(ret)]
        return {"customer_list": customer_list, "ret": list(ret)}

    def recent_month(self):
        today = datetime.datetime.now().date()
        one_week = datetime.datetime.now().date()-datetime.timedelta(weeks=4)
        customer_list = Customer.objects.filter(deal_date__gte=one_week,deal_date__lte=today)
        ret = UserInfo.objects.filter(depart_id=1, customers__deal_date__gte=one_week,customers__deal_date__lte=today).annotate(
            c=Count("customers")).values_list("username", "c")
        ret = [[item[0], item[1]] for item in list(ret)]
        return {"customer_list": customer_list, "ret": list(ret)}

    def get(self, request):
        context = None
        date = request.GET.get("date", "today")
        if hasattr(self, date):
            context = getattr(self, date)()
            print(context)
        return render(request, "customer/customers_statistics.html", context)
