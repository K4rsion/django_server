from django.urls import path
from .views import HomePageView, AboutPageView, PlotPageView, TextPageView1, TextPageView2, TextPageView3, TextPageView4, TextPageView5

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("plot/", PlotPageView.as_view(), name="plot"),
    path("text1/", TextPageView1.as_view(), name="text1"),
    path("text2/", TextPageView2.as_view(), name="text2"),
    path("text3/", TextPageView3.as_view(), name="text3"),
    path("text4/", TextPageView4.as_view(), name="text4"),
    path("text5/", TextPageView5.as_view(), name="text5"),
]
