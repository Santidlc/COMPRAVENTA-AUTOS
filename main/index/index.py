#############################
# Primer commit main COMPAVENTA-AUTOS
# *Subir a Github
# * Index.py
# ejecutable.exe
# release: 26/10/2022
# developer: Santiago De La Canal
##############################

from ast import While
from cgitb import reset
from operator import concat
from tkinter import N, Y

#main-resources
marca = "AUDI TT" , "AUDI A1" , "AUDI A2" , "AUDI A3" , "AUDI A4" , "AUDI A5" , "AUDI A6" , "AUDI Q1" , "AUDI Q2" , "AUDI Q3" , "AUDI Q4" , "BMW X1" , "BMW X2" , "BMW X3" , "BMW SERIE 1" , "BMW SERIE 2" , "BMW SERIE 3" , "BMW SERIE 4" , "BMW SERIE 5" , "BMW SERIE 6" , "BMW SERIE 7"

modelo = "2005" , "2006" , "2007" , "2008" , "2009" , "2010" , "2011" , "2013" , "2014" , "2015" , "2016" , "2015" , "2016" , "2017" , "2018" , "2020" , "2021" , "2022"

color = "rojo" , "negro" , "azul"

#index

#GUIA BASICA INPUT SIN VERIFICACION
marca = input('ingrese marca de su auto')
print ('usted quiere, ' + marca)

modelo = input('ingrese modelo del 2005 en adelante')
print ('usted quiere, ' + modelo)

color = input('ingrese color')
print ('usted quiere, ' + color)



while True:
        marca = input('ingrese marca de su auto')
        if talles != "AUDI":
            print("marca no valida")
        else:
            print("Genial contamos con esa marca")
            break
        continue

while True:
        marca = input('ingrese marca de su auto')
        if talles != "BMW":
            print("marca no valida")
        else:
            print("Genial contamos con esa marca")
            break
        continue

while True:
        modelo = input('ingrese modelo')
        if modelo != "0":
            print("elija un modelo del 2005 en adelante")
        else:
            print("tenemos ese modelo en stock")
            break
        continue

while True:
        color = input('ingrese marca de su auto')
        if talles != "rojo" "negro" "azul":
            print("no contamos con ese color")
        else:
            print("Genial, buena eleccion")
            break
        continue