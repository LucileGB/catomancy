from django.urls import include, path
from rest_framework import routers
from django.utils.safestring import mark_safe

from . import views


class GameRootView(routers.APIRootView):
    """
    Controls appearance of the API root view
    """
    def get_view_name(self):
        return "Game API"

    def get_view_description(self, html=False):
        text = "THis is a test"
        if html:
            return mark_safe(f"<p>{text}</p>")
        else:
            return text


class CatRouter(routers.DefaultRouter):
    APIRootView = GameRootView


router = CatRouter()
router.register(r'accounts', views.PlayerViewSet, basename='player_accounts')
router.register(r'cats', views.CatViewSet, basename='cats')


urlpatterns = [
    path('', include(router.urls)),
]