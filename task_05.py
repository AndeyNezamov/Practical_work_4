word = input('Введите текст: ').split(' ')
max_len = len(word[0])
for i in range(1, len(word)):
    if max_len < len(word[i]):
        max_len = len(word[i])

print(f'Самое длинное слово, {max_len} букв')