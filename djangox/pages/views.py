import time
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.shortcuts import render
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

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})