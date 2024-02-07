def calcular_media(lista_numeros):
    """
    Esta função calcula a média de uma lista de números.

    Args:
        lista_numeros (list): Uma lista de números para calcular a média.

    Returns:
        float: A média dos números na lista.
    """
    # Verifica se a lista está vazia
    if len(lista_numeros) == 0:
        return 0
    
    # Soma todos os números na lista
    soma = 0
    for numero in lista_numeros:
        soma += numero
    
    # Calcula a média
    media = soma / len(lista_numeros)
    return media

# Exemplo de uso da função
numeros = [10, 20, 30, 40, 50]
media = calcular_media(numeros)
print("A média é:", media)