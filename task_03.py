
row = int(input("Введите кол-во рядов: "))
seats = int(input("Введите кол-во сидений в ряде: "))
distance = int(input("Введите кол-во метров между рядами: "))
for _ in range(row):
    print(f"{'=' * seats} {'*' * distance} {'=' * seats}")