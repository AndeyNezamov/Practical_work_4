string = input('Введите a-свободное стойло или b-занятое стойло: ')
milk = 0
for i in range(10):
    if string[i] == 'b':
        milk += 2 * (i+1)
print(milk)
