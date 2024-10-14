nome = input('Olá! Para acessar a sua calculadora virtual primeiro digite seu nome: ')
print('Seja bem vindo', nome,'\n')
resposta1 = input('Você deseja somar, subtrair, dividir ou multiplicar ?''\n')

num1 = input('Digite o primeiro número:')
num2 = input('Agora o segundo número:')

convert1 = int(num1)
convert2 = int(num2)

soma = convert1 + convert2
sub = convert1 - convert2
divi = convert1 / convert2
mult = convert1 * convert2

if resposta1 == 'somar':
  print('Resultado:', soma)
  print('\n')
  resposta2 = input('Deseja repetir a operação, sim ou não?''\n')
  while resposta2 == 'sim':
    soma += convert2
    print('Resultado:', soma)
    print('\n')
    resposta2 = 'não'
    resposta2 = input('Deseja repetir a operação, sim ou não?''\n')

  else:
    print('Então acabamos por aqui, obrigado ≧◠‿◠≦✌')

elif resposta1 == 'subtrair':
  print('Resultado:', sub)
  print('\n')
  resposta2 = input('Deseja repetir a operação, sim ou não?''\n')
  while resposta2 == 'sim':
    sub -= convert2
    print('Resultado:', sub)
    print('\n')
    resposta2 = 'não'
    resposta2 = input('Deseja repetir a operação, sim ou não?''\n')

  else:
    print('Então acabamos por aqui, obrigado ≧◠‿◠≦✌')

elif resposta1 == 'dividir':
  print('Resultado:', divi)
  print('\n')
  resposta2 = input('Deseja repetir a operação, sim ou não?''\n')
  while resposta2 == 'sim':
    divi /= convert2
    print('Resultado:', divi)
    print('\n')
    resposta2 = 'não'
    resposta2 = input('Deseja repetir a operação, sim ou não?''\n')

elif resposta1 == 'multiplicar':
  print('Resultado:', mult)
  print('\n')
  resposta2 = input('Deseja repetir a operação, sim ou não?''\n')
  while resposta2 == 'sim':
    mult *= convert2
    print('Resultado:', mult)
    print('\n')
    resposta2 = 'não'
    resposta2 = input('Deseja repetir a operação, sim ou não?''\n')

  else:
    print('Então acabamos por aqui, obrigado ≧◠‿◠≦✌')
