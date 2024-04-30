"""import time

#Finonacci Iterativo

def iterativo(n):
    fib = [0, 1]
    
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]

n = int(input("Digite um número para calcular o Fibonacci: "))

#inicia o contador
start_time = time.time()

result = iterativo(n)

#finaliza o contador
end_time = time.time()
execution_time = end_time - start_time

print(f"O {n}-ésimo número de Fibonacci é: {result}\n")
print(f"Tempo de execução: {execution_time} segundos")

"""
import time
from decimal import Decimal

# Fibonacci Iterativo

def iterativo(n):
    a, b = 0, 1
    
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

n = int(input("Digite um número para calcular o Fibonacci: "))

# Inicia o contador
start_time = time.time()

result = iterativo(n)

# Finaliza o contador
end_time = time.time()
execution_time = end_time - start_time

print(f"O {n}-ésimo número de Fibonacci é: {Decimal(result)}\n")
print(f"Tempo de execução: {execution_time} segundos")
