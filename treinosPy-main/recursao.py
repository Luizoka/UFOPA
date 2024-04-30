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
