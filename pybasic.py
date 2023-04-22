teste = 2
print(teste)

## anotação

def soma_teste():
    soma = teste + 2
    print(soma)

soma_teste()

# string concatenation

print(f"aaaa {teste} ")


def nome_completo():
 primeiro_nome = input('Qual seu primeiro nome? ')
 sobrenome = input('Qual seu sobrenome? ')
 nome_inteiro = primeiro_nome + ' ' + sobrenome
 print(nome_inteiro)

nome_completo()


# function with parameters

def uma_funcao(parametro_entrada):
    print(parametro_entrada)

uma_funcao(teste)


# logic operators and type convertion

def verifica_se_pode_dirigir_sem_parametros():
  idade = input('Qual sua idade? ')
  idade = int(idade)
  if idade >= 18:
    print('Tem permissão para dirigir')
  else:
    print('Não tem permissão para dirigir')

verifica_se_pode_dirigir_sem_parametros()