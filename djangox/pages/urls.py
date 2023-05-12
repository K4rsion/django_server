from django.urls import path

from .views import HomePageView, AboutPageView, PlotPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("plot/", PlotPageView.as_view(), name="plot"),
]
