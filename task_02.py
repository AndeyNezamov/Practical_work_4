message = input()
for i in message:
    if i == '*':
        print(f'Символ «*» стоит на позиции {message.index(i)+1}')

