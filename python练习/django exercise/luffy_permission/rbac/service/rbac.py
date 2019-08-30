from rbac.models import Role


def initial_session(user, request):
    """
    功能：将当前登录人的所有权限录入session中
    :param user: 当前登录人
    """
    # 查询当前登录人的所有权限列表
    # 查看当前登录人的所有角色
    # ret=Role.objects.filter(user=user)
    permissions = Role.objects.filter(user=user).values("permissions__url",
                                                        "permissions__pk",
                                                        "permissions__title",
                                                        "permissions__pid",
                                                        "permissions__menu__title",
                                                        "permissions__menu__icon",
                                                        "permissions__menu__pk",
                                                        "permissions__name"
                                                        ).distinct()
    print("permissions", permissions)
    permissions_list = []
    permissions__name = []
    permissions_menu_dict = {}
    for item in permissions:
        # 权限列表
        permissions_list.append({
            "url": item["permissions__url"],
            "id": item["permissions__pk"],
            "pid": item["permissions__pid"],
            "title": item["permissions__title"],
        })
        permissions__name.append(item["permissions__name"])
        # 菜单权限列表
        menu_pk = item["permissions__menu__pk"]
        if menu_pk:
            if menu_pk not in permissions_menu_dict:
                permissions_menu_dict[menu_pk] = {
                    "menu_title": item["permissions__menu__title"],
                    "menu_icon": item["permissions__menu__icon"],
                    "children": [
                        {
                            "title": item["permissions__title"],
                            "url": item["permissions__url"],
                            "pk": item["permissions__pk"]
                        }
                    ]
                }
            else:
                permissions_menu_dict[menu_pk]["children"].append({
                    "title": item["permissions__title"],
                    "url": item["permissions__url"]
                })
    print("permissions_menu_dict", permissions_menu_dict)
    # 将当前登陆人的权限注入session中
    request.session["permissions_list"] = permissions_list
    # 将当前登陆人的菜单权限字典注入到session中
    request.session["permissions_menu_dict"] = permissions_menu_dict
    request.session["permissions__name"] = permissions__name
