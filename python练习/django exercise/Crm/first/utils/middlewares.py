from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class LoginMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path in ["/enter/", "/get_img/", "/register/"]:
            return None
        if not request.user.id:
            return redirect("/enter/")
