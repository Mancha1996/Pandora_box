#Caixa eletrônico
def caixa_eletronico():
    notas = [100, 50, 10, 5, 1]

    saque = int(input("Insira o valor do saque! valor entre 10 e 600 :"))

    if saque < 10 or saque > 600 : 
        print("Não foi possível completar a transção. Por favor Digite um valor entre 1 e 600!")
        return
    
    #dicionário
    qtd_notas = {}

    for nota in notas:
        quantidade = saque // nota #qntd de notas nesse valor
        if quantidade > 0 :
            qtd_notas[nota] = quantidade
            saque -= quantidade * nota #subtrai o valor das notas do total

    #exibe o resultado
    print("Notas fornecidas:")
    for nota , quantidade in qtd_notas.items():
        print(f"R$ {nota}: {quantidade} nota(s)")

caixa_eletronico()