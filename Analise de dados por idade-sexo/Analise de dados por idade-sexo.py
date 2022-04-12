tot18 = 0
toth = 0
totm20 = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo [M/F]: ').strip().upper()[0]
    if sexo == 'F' and idade <= 20:
        totm20 += 1
    if sexo == 'M':
        toth += 1
    if idade >= 18:
        tot18 += 1
    print('-' * 20)
    cont = ' '
    while cont not in 'SN':
        cont = input('Deseja continuar [S/N]? ').strip().upper()[0]
    if cont == 'N':
        break
print(f'O total com pessoas com mais de 18 anos é {tot18}')
print(f'O total de homens cadastrados foi {toth}')
print(f'O total de mulheres menores de 20 anos é {totm20}')
