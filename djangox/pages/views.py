import time
from bs4 import BeautifulSoup
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.shortcuts import render
import requests
from sympy import *
import numpy as np


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


class PlotPageView(TemplateView):
    template_name = "pages/plot.html"

    def post(self, request, *args, **kwargs):
        f = request.POST.get('function', '')
        x_values = np.linspace(-1000000, 1000000, 100)
        y_values = []
        x = symbols('x')
        expr = sympify(f)
        f_np = lambdify(x, expr, "numpy")

        for x_val in x_values:
            time.sleep(0.01)
            y_val = f_np(x_val)
            y_values.append(y_val)

        data = {"x_values": list(x_values), "y_values": list(y_values)}
        return JsonResponse(data)
    

class TextPageView(TemplateView):
    template_name = "pages/text.html"

    def get(self, request, *args, **kwargs):
        time.sleep(2)
        response = requests.get('http://az.lib.ru/g/gogolx_n_w/text_0140.shtml')
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        pre_tag = soup.find('xxx7')
        text = pre_tag.get_text()
        context = {'text': text}
        return render(request, self.template_name, context)