


from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect





class LoginMiddleWare(MiddlewareMixin):

    def process_request(self,request):

        if request.path in ["/login/","/reg/","/get_valid_img/"]:
            return None

        if not request.user.id:
            return redirect("/login/")



from django.conf import settings

class CurrentUserMiddleWare(MiddlewareMixin):

    def process_request(self,request):
        settings.CURRENT_USER_PK=request.user.pk



