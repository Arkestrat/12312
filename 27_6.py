n = int(input("Введите количество фильмов: "))
duration = []
for i in range(n):
    dur = int(input("Введите длительность {}-го фильма: ".format(i+1)))
duration.append(dur)

total_hours = sum(duration)
print("Общая длительность фильмов: {} часов".format(total_hours))
