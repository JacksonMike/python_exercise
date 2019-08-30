from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, render


class M1(MiddlewareMixin):

    def process_request(self, request):
        print("M1 process_request")

    def process_response(self, request, response):
        print("M1 process_response")
        # return HttpResponse("Sad")
        return response

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("M1 process_view")

    def process_exception(self, request, response):
        print("M1 process_exception...")


class M2(MiddlewareMixin):

    def process_request(self, request):
        print("M2 process_request")

    def process_response(self, request, response):
        print("M2 process_response")
        return response

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("M2 process_view")

    def process_exception(self, request, response):
        print("M2 process_exception...")
        return render(request, "error.html", {"error": response})
