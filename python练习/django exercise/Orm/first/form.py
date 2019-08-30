from django import forms
from django.forms import widgets as wid
from first.models import Publish, Author, Book


class BookForm(forms.Form):
    """校验数据 和 渲染页面"""
    title = forms.CharField(max_length=32)
    price = forms.IntegerField()
    # 从数据库中取数据
    publish = forms.ModelChoiceField(queryset=Publish.objects.all())
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for filed in self.fields.values():
            filed.widget.attrs.update({'class': 'form-control'})


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        labels = {
            "title": "书籍名称",
            "price": "价格",
            "publish": "出版商",
            "authors": "作者"
        }
        error_messages = {
            "title": {"required": "不能为空"},
            "price": {"required": "不能为空"},
            "publish": {"required": "不能为空"},
            "authors": {"required": "不能为空"},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            # filed.error_messages={"required":"不能为空"}
            field.widget.attrs.update({'class': 'form'})
