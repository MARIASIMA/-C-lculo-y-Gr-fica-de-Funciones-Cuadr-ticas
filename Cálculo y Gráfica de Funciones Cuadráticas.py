import numpy as np
import matplotlib.pyplot as plt

def funcion_cuadratica(a, b, c, x):
    """
    Calcula el valor de f(x) = ax^2 + bx + c
    """
    return a * x**2 + b * x + c

def graficar_funcion_cuadratica(a, b, c):
    """
    Genera y grafica una función cuadrática en el rango de x definido.
    """
    # Crear un rango de valores de x
    x = np.linspace(-10, 10, 400)
    # Calcular el valor de y para cada valor de x
    y = funcion_cuadratica(a, b, c, x)
    
    # Crear la gráfica
    plt.figure(figsize=(8,6))
    plt.plot(x, y, label=f'{a}x² + {b}x + {c}')
    
    # Añadir etiquetas y título
    plt.title(f'Gráfica de la función cuadrática: {a}x² + {b}x + {c}')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    
    # Dibujar el eje X y Y
    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(0, color='black',linewidth=1)
    
    # Añadir la leyenda
    plt.legend()
    
    # Mostrar la gráfica
    plt.grid(True)
    plt.show()

# Pedir al usuario los coeficientes
a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))

# Llamar a la función para graficar
graficar_funcion_cuadratica(a, b, c)
