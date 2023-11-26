names_yesterday = ["Александр", "Петр", "Лев", "Мария", "Елизавета", "Юлия"]
names_today = []

name = input("Введите имя персонажа (или END для окончания): ")
while name != "END":
    names_today.append(name)
name = input("Введите имя персонажа (или END для окончания): ")

count = 0
for name in names_today:
    if name in names_yesterday:
            count += 1

print("Количество имен в сегодняшнем фильме, совпадающих с именами вчерашнего фильма:", count)
