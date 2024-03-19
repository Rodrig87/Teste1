def fibonacci_sequence(n):
    fibonacci = [0, 1]
    while fibonacci[-1] <= n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

def verifica_numero_fibonacci(numero):
    fibonacci = fibonacci_sequence(numero)
    if numero in fibonacci:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."


numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))


print(verifica_numero_fibonacci(numero))
