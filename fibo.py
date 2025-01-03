# Generar los primeros 'n' números de Fibonacci
def fibonacci_iterativo(n):
    secuencia = []
    a, b = 0, 1
    for _ in range(n):
        secuencia.append(a)
        a, b = b, a + b
    return secuencia

# Ejemplo de uso
n = 10
print(f"Secuencia de Fibonacci (primeros {n} números): {fibonacci_iterativo(n)}")
