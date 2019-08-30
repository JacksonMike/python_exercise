from first.models import Role


def initial_session(request, name):
    """将当前登陆人的权限录入session中"""
    permissions_queryset = Role.objects.filter(user__name=name).values("permissions__url").distinct()
    print(permissions_queryset)
    permissions_list = []
    for j in permissions_queryset:
        permissions_list.append(j["permissions__url"])
    print(permissions_list)
    request.session["permissions_list"] = permissions_list
