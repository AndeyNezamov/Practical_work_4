res = []
for _ in range(10):
    word = input('Какое слово крикнешь? ')
    if word.title() == "Карамба":
        res.append(word)
print(f'{len(res)} человек присоединятся к команде')
