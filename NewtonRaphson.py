#Librerias
import math

# Funcion base y su derivada 
def f(x):
    return math.exp(-x) - x

def df(x):
    return -math.exp(-x) - 1
    
#Iteraciones de Newton Raphson
def newton_raphson(xo, tolerancia=0.001, max_iter=10):
    print(f"{'i':<6} {'xᵢ':<12} {'f(xᵢ)':<14} {'f′(xᵢ)':<14} {'|xᵢ - xᵢ₋₁|'}")
    print("-" * 60)
    print(f"{'0':<6} {xo:<12.6f} {f(xo):<14.6f} {df(xo):<14.6f} {'---'}")

    x_actual = xo
    for i in range(1, max_iter + 1):
        fx   = f(x_actual)
        dfx  = df(x_actual)


        x_nuevo = x_actual - fx / dfx
        error   = abs(x_nuevo - x_actual)

        print(f"{i:<6} {x_nuevo:<12.6f} {f(x_nuevo):<14.6f} {df(x_nuevo):<14.6f} {error:<.6f}")

        if error < tolerancia:
            print("-" * 60)
            print(f"\nConvergencia alcanzada en la iteración {i}")
            print(f"  Raíz aproximada: x ≈ {x_nuevo:.6f}")
            print(f"  f({x_nuevo:.6f}) ≈ {f(x_nuevo):.10f}")
            break

        x_actual = x_nuevo

#Valores de entrada
xo         = 0.5
tolerancia = 0.001

#Ejecutando la funcion principal
newton_raphson(xo, tolerancia)