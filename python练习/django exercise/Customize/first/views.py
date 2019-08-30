from django.shortcuts import render


# Create your views here.
def index(request):
    n = 10
    val = "Apple"
    # return render(request, "third/index.html", locals())
    return render(request, "index.html", locals())
