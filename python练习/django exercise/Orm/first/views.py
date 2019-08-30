from django.shortcuts import render, redirect
from first.models import Book
from first.form import BookForm, BookModelForm
from django import forms


# Create your views here.
def book_view(request):
    book_list = Book.objects.all()
    return render(request, "book_view.html", locals())


def book_add(request):
    if request.method == "GET":
        form = BookModelForm()
        return render(request, "book_add.html", locals())
    else:

        form = BookModelForm(request.POST)
        if form.is_valid():
            # authors=form.cleaned_data.pop("authors")
            # book = Book.objects.create(**form.cleaned_data)
            # book.authors.add(*authors)
            form.save()
            return redirect("/book/")
        else:
            return render(request, "book_add.html", locals())


def book_edit(request, edit_id):
    edit_book = Book.objects.filter(nid=edit_id).first()
    if request.method == "GET":
        form = BookModelForm(instance=edit_book)
        return render(request, "book_edit.html", locals())

    else:
        form = BookModelForm(request.POST, instance=edit_book)
        if form.is_valid():
            form.save()
            return redirect("/book/")
        else:
            return render(request, "book_edit.html", locals())