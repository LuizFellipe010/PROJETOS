#Aula  01 String Python
#int = número inteiro
#float = variavel decimal vem de ponto flutuante (3.72) deve ser com ponto e não virgúla
#string = tipo texto
#boolean = variavel de verdadeiro ou falso (true or false)


faturamento = 1000 
desconto = 300
lucro = faturamento - desconto
print("o faturamento foi de", faturamento)
print("o desconto foi de", desconto)
print("o lucro foi de", lucro)

# Aula 02
faturamento = 1000 
desconto = 300
lucro = faturamento - desconto
margem_lucro = lucro / faturamento

print(f"Faturamento da Empresa: {faturamento}, Custo: {desconto}, Lucro {lucro}")

email_cliente = "qualquercoisaaleatoria@gmail.com"

# maiscula
email_cliente = email_cliente.upper()
print(email_cliente)
# minuscula
email_cliente = email_cliente.lower()
print(email_cliente)

# comando usado para localizar o "@" # -1 quando não encontrar
print(email_cliente.find("@"))

# tamanho do texto
print(len(email_cliente))

# pegar um caractere ele considera o texto como lista e pega a localização que for denominada 0=q 1=u
print(email_cliente[0])

# pega até 20 caracteres
print(email_cliente[1:20])
print(email_cliente[:20])

# trocar um pedaço do texto
novo_email = email_cliente.replace("@gmail.com","@outlook.com")
print(novo_email)

nome = "luiz fellipe"
#trabalhar com nomes
print(nome.capitalize())
print(nome.title())

#pegar o servidor do email
posicao_arroba = email_cliente.find("@") # +1 seria para não incluir o arroba na variavel
servidor = email_cliente[posicao_arroba:] 
#servidor = email_cliente[22:32]
print(servidor)

#pegar o 1 nome
posicao_espaço = nome.find(" ")
nomelocaliza = nome[:posicao_espaço]

#pegar o sobrenome
sobrenome = nome[posicao_espaço+1:]
print(nomelocaliza)
print(sobrenome)

#casos especiais : formatações númericas em texto
margem_lucro = round(margem_lucro, 2) #rodar sem o .0% para ver o resultado
print(f"Faturamento da Empresa: R${faturamento:.2f}, Custo: R${desconto:.2f}, Lucro R${lucro}, Margem R${margem_lucro:.0%}")
# este .0% serve para o arrdondamento da casa decimal e round serve para determiar uqantas casas o número deve mostrar
# f = float siginifica que a variavel é tipo float

# Aula 03 Inputs e Listas - cls deleta histórico do terminal do vscode
# INPUTS

'''email = input("Escreva seu e-mail: ")
nome = input("Escreva seu Nome: ")

print(nome, email) # Caso você peça para alocar um número no input ele considera o input como texto, meso sendo um valor e no momento que você faça uma conta ela não vai fazer a conta

print(f"{nome} Verifique seu -mail: {email} que enviamos um link de confirmação")'''


#LISTAS
vendas = [100 , 50, 14, 20, 30, 700] #Isto é uma Litsa no Python

total_vendas = sum(vendas) # soma o valor de vendas
print(total_vendas)

#tamanho da lista
quantidade_vendas = len(vendas) #lengh
print(quantidade_vendas)