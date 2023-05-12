from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path(_("admin/"), admin.site.urls),
    path(_("accounts/"), include("allauth.urls")),
    path(_(""), include("pages.urls")),
)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
