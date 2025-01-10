#Verificar se um número pertence à sequência de Fibonacci

def is_fibonacci(number):
    a, b = 0, 1
    while b < number:
        a, b = b, a + b
    return b == number or number == 0

# Teste com entrada
number = int(input("Informe um número: "))
if is_fibonacci(number):
    print(f"O número {number} pertence à sequência de Fibonacci.")
else:
    print(f"O número {number} NÃO pertence à sequência de Fibonacci.")
