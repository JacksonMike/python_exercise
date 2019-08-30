from django.urls import path, re_path

from second.views import BookView, BookEditView, BookModelView, PageView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'^index', BookModelView)

# self.registry = [(prefix, viewset)]

urlpatterns = [

    # path('index/', BookView.as_view()),
    # re_path('index/(\d+)', BookEditView.as_view()),

    # path('index/', BookModelView.as_view({'get': 'list', 'post': 'create'})),
    # re_path('index/(?P<pk>\d+)', BookModelView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    path('page/', PageView.as_view())
]
urlpatterns += router.urls
