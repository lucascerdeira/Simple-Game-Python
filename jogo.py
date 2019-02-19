from random import randint
c = ''
name = input('Digite o seu nome: ').capitalize().strip()
print('-='*25)
print('     Tente adivinhar um número entre 0 e 10')
print('-='*25)
print(f'{name}, Você tem 5 vidas para ganhar')
victory = 0
game_over = 0
for attempt in range(1, 6):
    computer = randint(0, 10)
    print('-='*20)

    user = int(input('Faça seu chute entre 0 e 10: '))
    print('-='*20)
    if user == computer:
        print(f'{C:^20}Jogador {name} Venceu!')
        victory += 1

    else:
        print(f'{c:^20}Jarvis venceu')
        game_over += 1

print(f'Vitorias {victory}, Derrotas {game_over} ')