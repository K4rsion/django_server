from django.urls import path
from .views import HomePageView, AboutPageView, PlotPageView, TextPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("plot/", PlotPageView.as_view(), name="plot"),
    path("text/", TextPageView.as_view(), name="text"),
]
