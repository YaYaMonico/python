# Usando o laço for
for andar in range(20, 0, -1):  # Começa do 20 e vai até o 1, decrementando de -1 em -1
    if andar != 13:  # Exclui o 13º andar
        print(andar)
        
# Usando o laço while
andar = 20
while andar >= 1:
    if andar != 13:
        print(andar)
    andar -= 1
