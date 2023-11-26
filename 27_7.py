prev = int(input("Введите длительность первой сцены: "))
next_scene = prev * 2

while next_scene != -1:
    current_scene = int(input("Введите длительность следующей сцены: "))

    if current_scene != next_scene:
        print("NO")
        break

    next_scene = current_scene * 2

else:
    print("YES")
