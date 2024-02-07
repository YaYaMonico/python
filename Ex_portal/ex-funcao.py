def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 != 0:  # Verifica se o segundo número é diferente de zero para evitar a divisão por zero
            return num1 / num2
        else:
            return "Erro: divisão por zero"
    else:
        return 0  # Retorna 0 se a operação não existir

# Exemplo de uso da função:
resultado = calculadora(10, 5, 1)  # Soma: 10 + 5
print("Resultado da soma:", resultado)

resultado = calculadora(10, 5, 2)  # Subtração: 10 - 5
print("Resultado da subtração:", resultado)

resultado = calculadora(10, 5, 3)  # Multiplicação: 10 * 5
print("Resultado da multiplicação:", resultado)

resultado = calculadora(10, 0, 4)  # Divisão: 10 / 0 (irá retornar erro de divisão por zero)
print("Resultado da divisão:", resultado)

resultado = calculadora(10, 5, 5)  # Operação inválida (irá retornar 0)
print("Resultado da operação inválida:", resultado)
