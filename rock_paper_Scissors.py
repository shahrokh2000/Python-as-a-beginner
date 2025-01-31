from random import randint
m=int(input('m='))
n=int(input('number of sets to win:'))
a=0
b=0
while not (a==n or b==n):
    player_1=input('play:')
    while not (player_1=='rock' or player_1=='paper' or player_1=='scissors'):
        player_1=input('play:')


    r=randint(1,3)
    if r==1:
        player_2='rock'
        print(f'computer:{player_2}')
    elif r==2:
        player_2='paper'
        print(f'computer:{player_2}')
    elif r==3:
        player_2='scissors'
        print(f'computer:{player_2}')

    if player_1==player_2:
        print('draw')
    elif player_1=='rock' and player_2=='paper':
        print('you lose')
        b=b+1
    elif player_1=='rock' and player_2=='scissors':
        print('you won')
        a=a+1
    elif player_1=='paper' and player_2=='scissors':
        print('you lose')
        b=b+1
    elif player_1=='paper' and player_2=='rock':
        print('you won')
        a=a+1
    elif player_1=='scissors' and player_2=='rock':
        print('you lose')
        b=b+1
    elif player_1=='scissors' and player_2=='paper':
        print('you won')
        a=a+1
    if  m==1:
        if n-1==a and n-1==b and n!=1:
            n=n+1

if n==0:
    print('goodbye')
else:
    if a==n:
        print(f'----------------\nyou={a} computer={b}\nyou won the Game')
    elif b==n:
        print(f'----------------\nyou={a} computer={b}\nyou lost the Game')
