from django.urls import include, path
from rest_framework import routers

from . import views

class CatRouter(routers.DefaultRouter):
    def get_api_root_view(self, api_urls=None):
        root_view = super(CatRouter, self).get_api_root_view(api_urls=api_urls)
        root_view.cls.__doc__ = "This is the core "
        return root_view

router = CatRouter()
router.register(r'cats', views.CatViewSet, basename='cats')

urlpatterns = [
    path('', include(router.urls)),
]