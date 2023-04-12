from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("pages.urls")),
    path("plot/", views.plot, name="plot"),
]

urlpatterns += i18n_patterns(
    # URL-шаблоны для локализованных приложений
    path(_("admin/"), admin.site.urls),
    path(_("accounts/"), include("allauth.urls")),
    path(_(""), include("pages.urls")),
    path(_("plot/"), views.plot, name="plot"),
)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
