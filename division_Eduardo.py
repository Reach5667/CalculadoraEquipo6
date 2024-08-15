# -*- coding: utf-8 -*-
"""Calculadora.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1j0Lwo4y3tk9K5CcmmsCH-WNaJ3GWFL1b
"""

def divide_numbers():
    try:

        numerator = float(input("Escribe el numerador: "))
        denominator = float(input("Escribe el denominador: "))


        result = numerator / denominator


        print(f"El resultado de {numerator} / {denominator} es: {result}")

    except ZeroDivisionError:

        print("Error: La division entre 0 no es posible.")

    except ValueError:

        print("Error: Por favor ingrese solo valores numericos.")

divide_numbers()