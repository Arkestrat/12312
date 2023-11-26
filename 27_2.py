line = input()
flag = 1
while line != "":
    if "любовь" in line or "кровь" in line:
        flag = 0
        break
    line = input()
if flag == 1:
    print("ХОРОШЕЕ")
else:
    print("НЕ ХОРОШЕЕ")