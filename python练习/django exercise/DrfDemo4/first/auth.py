from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import User


class MyAuth(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get("token", "")
        if not token:
            raise AuthenticationFailed("缺少token")
        user_obj = User.objects.filter(token=token).first()
        if not user_obj:
            raise AuthenticationFailed("token不合法")
        return (user_obj, token)
