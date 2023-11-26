n = int(input("Введите количество строк: "))
m = int(input("Введите количество чисел в строке: "))

for i in range(n):
    for j in range(1, m + 1):
        print(j, end=" ")
    print()