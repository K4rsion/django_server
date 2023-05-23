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
    

class TextPageView1(TemplateView):
    template_name = "pages/text/text1.html"

    def get(self, request, *args, **kwargs):
        time.sleep(2)
        response = requests.get('http://az.lib.ru/g/gogolx_n_w/text_0140.shtml')
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        pre_tag = soup.find('xxx7')
        text1 = pre_tag.get_text()
        context = {'text1': text1}
        return render(request, self.template_name, context)
    
class TextPageView2(TemplateView):
    template_name = "pages/text/text2.html"

    def get(self, request, *args, **kwargs):
        time.sleep(2)
        response = requests.get('http://az.lib.ru/g/gonkur_z_e/text_1867_manette_salomon-oldorfo.shtml')
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        pre_tag = soup.find('xxx7')
        text2 = pre_tag.get_text()
        context = {'text2': text2}
        return render(request, self.template_name, context)
    
class TextPageView3(TemplateView):
    template_name = "pages/text/text3.html"

    def get(self, request, *args, **kwargs):
        time.sleep(2)
        response = requests.get('http://az.lib.ru/g/gonkur_z_e/text_1877_la_fille_elisa-oldorfo.shtml')
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        pre_tag = soup.find('xxx7')
        text3 = pre_tag.get_text()
        context = {'text3': text3}
        return render(request, self.template_name, context)
    
class TextPageView4(TemplateView):
    template_name = "pages/text/text4.html"

    def get(self, request, *args, **kwargs):
        time.sleep(2)
        response = requests.get('http://az.lib.ru/w/wega_l_d/text_1897_poslednyaya_lubov_lope_de_vega-oldorfo.shtml')
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        pre_tag = soup.find('xxx7')
        text4 = pre_tag.get_text()
        context = {'text4': text4}
        return render(request, self.template_name, context)
    
class TextPageView5(TemplateView):
    template_name = "pages/text/text5.html"

    def get(self, request, *args, **kwargs):
        time.sleep(2)
        response = requests.get('http://az.lib.ru/m/mann_g/text_1907_zwischen_den_rassen-oldorfo.shtml')
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        pre_tag = soup.find('xxx7')
        text5 = pre_tag.get_text()
        context = {'text5': text5}
        return render(request, self.template_name, context)