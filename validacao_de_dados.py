from py_compile import main


##salario = float(input("Digite seu salario :"))
#sexo = str(input("Digite seu sexo f ou m:"))
#estado_civil = str(input("Digite seu estado civil c , s , d , v :"))

##VALIDAÇÃO DO NOME

def validação_nome():
 
    while True:
        nome = str(input("Digite seu nome :"))
        if len(nome) >= 3 and len(nome) < 100:
            return nome
        else:
            print(f"O nome deve estar entre 3 e 100 caracteres")
nome = validação_nome()
    

##VALIDAÇÃO DA IDADE

def validacao_idade():
    while True :
        idade = int(input("Digite sua idade :"))
        if idade > 0 and idade < 150 :
            return idade
        else:
            print(f"a idade deve ser entre 1 e 150")
idade = validacao_idade()   

#validação do salario deve ser maior que zero
def validacao_salario():
    while True:
        salario = float(input("Digite seu salário :"))
        if salario > 0 :
            return salario
        else:
            print("O valor inválido!")
salario = validacao_salario()

##validação de sexo 
def validacao_sexo():
    while True:
        sexos = ["M" , "F"] #lista de sexos
        sexo = str(input("Insira o seu sexo M para masculino e F para feminino :")).upper()
        if sexo in sexos :
            return sexo 
        else : 
            print("Digite um Sexo válido!")
sexo = validacao_sexo()

## validaçaõ de estado civil
def validacao_estadocivil():
    while True:
        estados_civis = ["C" , "S", "D", "V"]
        estado = str(input("Insira o seu estado civil, C para casado(a), S para solteiro(a), D para divorciado(a) e V para viuvo(a)")).upper()
        if estado in estados_civis :
            return estado
        else:
            print("Digite um valor válido")
estado = validacao_estadocivil()

##Hora dos prints
print(f"nome:{nome} // idade:{idade} // sexo: {sexo} // Salario: {salario} // Estado Civil: {estado}");