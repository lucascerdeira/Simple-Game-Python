from random import randint #PODERIA TER FEITO COM MENAS LINHAS
x = 0                       #Tem que fazer melhorias mas é assim mesmo, código de 2019 
y = ''
print('-=-' * 25)
print(f'{y:^20}VAMOS JOGAR PAR OU IMPAR')
while True:
    print('-=-' * 25)
    computador = randint(0, 10)
    número = int(input('Informe um valor: '))
    par_ou_impar = str(input('\033[1;31;0mPAR / IMPAR: \033[m ')).strip().upper()[0]
    print(par_ou_impar)
    soma = computador + número
    if soma % 2 == 0:
        print(f'Você jogou {número} e o computador {computador}. Total de {soma} deu PAR')
        if par_ou_impar == 'I' and soma % 2 == 1:
            print('VITÓRIA')
            x += 1
        elif par_ou_impar == 'P' and soma % 2 == 0:
            print('VITÓRIA')
            x += 1

        elif par_ou_impar == 'I' and soma % 2 == 0:
            print('DERROTA')
            break
        elif par_ou_impar == 'P' and soma % 2 == 1:
            print('DERROTA')
            break
    elif soma % 2 == 1:
        print(f'Você jogou {número} e o computador {computador}. Total de {soma} deu IMPAR')
        if par_ou_impar == 'I' and soma % 2 == 1:
            print('VITÓRIA')
            x += 1
        elif par_ou_impar =='P' and soma % 2 == 0:
            print('VITÓRIA')
            x += 1
        elif par_ou_impar == 'I' and soma % 2 == 0:
            print('DERROTA')
            break
        elif par_ou_impar == 'P' and soma % 2 == 1:
            print('DERROTA')
            break
        elif par_ou_impar != 'PM':
            print('PAR OU IMPAR [P/I]')

print(f'GAME OVER! VOCÊ VENCEU {x} VEZES!')
