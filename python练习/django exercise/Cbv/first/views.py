from django.shortcuts import render, HttpResponse
from django.views import View


# Create your views here.


class EnterView(View):
    # def dispatch(self, request, *args, **kwargs):
    #     print("dispatch")
    #     ret = super().dispatch(request, *args, **kwargs)
    #     return ret

    def get(self, request):
        return render(request, "enter.html")

    def post(self, request):
        return HttpResponse("post")
