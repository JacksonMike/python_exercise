
from django.urls import path
from .views import BookView

urlpatterns = [
    path('index/', BookView.as_view())
]
