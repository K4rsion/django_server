from django.shortcuts import render
from sympy import *
import numpy as np
from django.http import JsonResponse
import time

def plot(request):
    
    if request.method == "POST":
        # Получаем пользовательскую функцию f(x)
        f = request.POST.get('function', '')
        x_values = np.linspace(-1000000, 1000000, 100) #задать область определения
        y_values = []

        # Преобразование символьного выражения в функцию
        x = symbols('x')
        expr = sympify(f)
        f_np = lambdify(x, expr, "numpy")

        # Вычисляем значение f(x) для каждого значения x
        for x_val in x_values:
            time.sleep(0.01)  # Приостановить выполнение
            y_val = f_np(x_val)
            y_values.append(y_val)

        # Отправляем результат в формате JSON на клиент
        data = {"x_values": list(x_values), "y_values": list(y_values)}
        return JsonResponse(data)
    else:
        return render(request, "plot.html")