# Ghost game
from random import randint
from time import sleep
print('Ghost game')
feeling_brave = True
score = 0
while feeling_brave:
    ghost_door = randint(1,3)
    print('Three doors ahead... \nA ghost behind one')
    print('Which door do you open?')
    door = input('1, 2 or 3?')
    door_num = int(door)
    if door_num == ghost_door:
        sleep(0.5)
        print('GHOST!')
        feeling_brave = False
    else:
        sleep(0.5)
        print('No ghost!')
        print('You enter the next room')
        score = score + 1
print('Run away!')
print('Game over! You scored:',score)
sleep(3)