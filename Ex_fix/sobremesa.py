#Variáveis relacionadas à sobremesa favorita
sobremesa_favorita = "Pudim"
preco_sobremesa = 30
quantidade_convidados = 5 #considerar o anfitrião + 4 convidados

#Calculando o novo valor total
quantidade_almocos = 4
quantidade_bebidas = 3
quantidade_sobremesas = 2

#Calculando os custos individuais
preco_almoco = 40
preco_bebida = 20
orcamento = 200
custo_total = (preco_almoco * quantidade_almocos) + (preco_bebida * quantidade_bebidas) + (preco_sobremesa * quantidade_sobremesas)
custo_por_convidado = custo_total / quantidade_convidados

#Exibir as informações sobre a sobremesa
print("Sobremesa favorita:", sobremesa_favorita)
print("Preco da sobremesa:", preco_sobremesa)
print("Quantidade de convidados:", quantidade_convidados)
print()

#Exibir os resultados dos calculos
print("Novo valor total (almoços, bebidas e sobremesas):", custo_total)
print("Valor a ser pago por cada convidado:", custo_por_convidado)
print("O que eu tenho na carteira:", orcamento)