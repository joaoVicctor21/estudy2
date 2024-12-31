valor_saque = int(input("Digite o valor do saque: "))
saldo = 10000

if valor_saque > saldo: 
    print("saldo insuficiente")
else:
    saldo -= valor_saque
    print(f"você sacou {valor_saque}, seu saldo atual é {saldo}")

aluno = input("digite o nome do aluno: ")
nota1 = float(input("digite a primeira nota:"))
nota2 = float(input("digite a segunda nota:"))
nota3 = float(input("digite a TERCEIRA nota:"))

media = (nota1 + nota2 +nota3)/ 3

if media >= 7 :
    print(f"o aluno {aluno}, passou de ano")
elif media <7 and media>4:
    print(f"o aluno {aluno} ficou em recuperação")
else:
    print(f"o aluno {aluno} reprovou")


numero = int(input("digite um numero"))
impar_par = numero % 2

if impar_par != 0:
    print(f"o numero {numero} é impar")
else:
    print(f"o numero {numero }é par")

curso = "python"

print(curso.center(12,"@"))

print("@".join(curso))

nome = "jota rodrigues"
idade = 210
trabalho = "programador"

print("ola me chamo {} tenho {} anos e trabalho como {}".format(nome,idade,trabalho))

print(nome[::2])

nome = "joca"

mensagem = f"""
olá meu nome é {nome},

eu estou aprendendo python
"""
print(mensagem)
def verificador_ano_bissexto():
    ano = int(input())  # Lê o ano fornecido pelo usuário

    # Verifica se o ano é bissexto
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print("SIM")
    else:
        print("NÃO")

#Chama a função para realizar a verificação
verificador_ano_bissexto()

def verificador_ano_bissexto():
    ano = int(input())

# TODO: Verifique se o ano é bissexto utilizando uma estrutura de controle condicional, como if/else:




    if (ano % 4 ==0 and ano % 100 != 0) or (ano % 400 == 0):
      print("SIM")
    else:
      print("NÃO")
  
verificador_ano_bissexto()

carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros):
    print(f"{indice}:{carro}")

numeros = [1,2,5,7,4,89,34,656,965,233]
pares = [numero for numero in numeros if numero %2 != 0]
print(pares)

numeros2 = [ 12,3454,323,4,6,3,2]
subtracao = [numero2 -1 for numero2 in numeros2]
print(subtracao)
        