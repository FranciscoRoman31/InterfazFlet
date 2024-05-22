import flet as ft
import numpy as np
from flet import (
    Column,
    Container,
    ElevatedButton,
    Page,
    Row,
    Text,
    border_radius,
    colors,
)

container = ft.Container

def main(page: ft.page):
    def add_clicked(e):
        page.add(ft.Checkbox(label=numero.value))
        numero.value = ""
        page.update()

    numero = ft.TextField(hint_text="Ingrese el numero y seleccione su base", expand=True)
    page.add(numero)
    decimal = ft.ElevatedButton("Decimal")
    binario = ft.ElevatedButton("Binario")
    octal = ft.ElevatedButton("Octal")
    hexa = ft.ElevatedButton("Hexadecimal")
    terna = ft.ElevatedButton("Ternario")
    cuat = ft.ElevatedButton("Cuaternario")
    botones = ft.Column()
    view=ft.Column(
        width=600,
        controls=[
            ft.Row(
                page.add(decimal), page.add(binario), page.add(octal), page.add(hexa), page.add(terna), page.add(cuat)
            ),
            botones,
        ],
    )

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(view)

#Funciones para convertir las bases

def convertir_a_decimal(numero, base):
    if base < 1 or base > 16:
        raise ValueError("La base debe estar entre 1 y 16")

    numero_decimal = 0
    potencia = 0

    while numero > 0:
        ultimo_digito = numero % 10
        equivalente_decimal = ultimo_digito * (base ** potencia)
        numero_decimal += equivalente_decimal
        potencia += 1
        numero //= 10

    return numero_decimal

def convertir_a_terniario(numero, base):
    if base < 1 or base > 16:
        raise ValueError("La base debe estar entre 1 y 16")
    
    numero_terniario = ""
    while numero > 0:
        numero_terniario = str(numero % 3) + numero_terniario
        numero //= 3
    
    return numero_terniario

def convertir_a_cuaterniario(numero, base):
    if base < 1 or base > 16:
        raise ValueError("La base debe estar entre 1 y 16")
    
    numero_cuaterniario = ""
    while numero > 0:
        numero_cuaterniario = str(numero % 4) + numero_cuaterniario
        numero //= 4
    
    return numero_cuaterniario

def convertir_a_hexadecimal(numero, base):
    if base < 1 or base > 16:
        raise ValueError("La base debe estar entre 1 y 16")

    digitos_hexadecimales = "0123456789ABCDEF"
    numero_hexadecimal = ""

    while numero > 0:
        residuo = numero % 16
        digito_hexadecimal = digitos_hexadecimales[residuo]
        numero_hexadecimal = digito_hexadecimal + numero_hexadecimal
        numero //= 16

    return numero_hexadecimal

def convertir_a_octal(numero, base):
    if base < 1 or base > 16:
        raise ValueError("La base debe estar entre 1 y 16")

    numero_octal = ""

    while numero > 0:
        digito = numero % 8
        numero_octal = str(digito) + numero_octal
        numero //= 8

    return numero_octal

def convertir_a_binario(numero, base):
    if base < 1 or base > 16:
        raise ValueError("La base debe estar entre 1 y 16")

    numero_binario = ""

    while numero > 0:
        digito = numero % 2
        numero_binario = str(digito) + numero_binario
        numero //= 2

    return numero_binario

#Funciones para realizar la eliminacion de Gauss Jordan

A = np.array([[4,2,5],
              [2,5,8],
              [5,4,3]])

B = np.array([[60.70],
              [92.90],
              [56.30]])

casicero = 1e-15

A = np.array(A,dtype=float) 

AB  = np.concatenate((A,B),axis=1)
AB0 = np.copy(AB)

size = np.shape(AB)
n = size[0]
m = size[1]

for i in range(0,n-1,1):
    colum  = abs(AB[i:,i])
    max = np.argmax(colum)
    if (max !=0):
        temporal = np.copy(AB[i,:])
        AB[i,:] = AB[max+i,:]
        AB[max+i,:] = temporal
AB1 = np.copy(AB)

for i in range(0,n-1,1):
    pivot = AB[i,i]
    adelante = i + 1
    for k in range(adelante,n,1):
        factor  = AB[k,i]/pivot
        AB[k,:] = AB[k,:] - AB[i,:]*factor

ultfila = n-1
ultcolum = m-1
X = np.zeros(n,dtype=float)

for i in range(ultfila,0-1,-1):
    suma = 0
    for j in range(i+1,1):
        suma = suma + AB[i,ultcolum,j]*X[j]
    b = AB[i, ultcolum]
    X[i] = (b-suma)/AB[i,i]

X = np.transpose([X])

print('Matriz aumentada:')
print(AB0)
print('Pivoteo parcial por filas')
print(AB1)
print('eliminación hacia adelante')
print(AB)
print('solución: ')
print(X)

ft.app(target=main)

ft.app(target=main)
