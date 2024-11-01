first_coordinate = 8
second_coordinate = 10
flag = True
while flag:
    print(f'Марсоход находится на позиции {first_coordinate}, {second_coordinate}, введите команду:')
    button = input('')
    if -1 <= first_coordinate <= 16:
        if button.lower() == 'a':
            first_coordinate -= 1
            if first_coordinate == -1:
                first_coordinate = 0
        elif button.lower() == 'd':
            first_coordinate += 1
            if first_coordinate == 16:
                first_coordinate = 15
        

    if -1 <= second_coordinate <= 21:
        if button.lower() == 's':
            second_coordinate -= 1
            if second_coordinate == -1:
                second_coordinate = 0
        elif button.lower() == 'w':
            second_coordinate += 1
            if second_coordinate == 21:
                second_coordinate = 20
    
    if button == '0':
        break