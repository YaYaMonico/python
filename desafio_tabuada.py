# Solicitar ao usuário para inserir um número
numero = int(input("Digite um número para ver a sua tabuada: "))

# Calcular e imprimir a tabuada
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
