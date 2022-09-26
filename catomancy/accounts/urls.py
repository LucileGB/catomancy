from django.urls import include, path
from rest_framework import routers
from django.utils.safestring import mark_safe

from . import views


class AccountRootView(routers.APIRootView):
    """
    Controls appearance of the API root view
    """
    def get_view_name(self):
        return "Account Root"

    def get_view_description(self, html=False):
        text = "This is the root for account management."
        if html:
            return mark_safe(f"<p>{text}</p>")
        else:
            return text


class AccountRouter(routers.DefaultRouter):
    APIRootView = AccountRootView


router = AccountRouter()
router.register(r'accounts', views.AccountViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]