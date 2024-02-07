print("Digite seu nome:")
nome = input()
executar = True
while executar:
    print("Digite seu ano de nascimento")
    try:
        ano = int(input())
        if ano < 1922 or ano > 2021:
            print("O ano precisa ser entre 1922 e 2021")
        else:
            idade = 2022 - ano
            print("O usuário", nome, "completou ou completará", idade, "anos de idade em 2022")
            executar = False
    except ValueError:
        print("Os anos precisam ser escritos apenas com números")
