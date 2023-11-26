a, b = int(input()), int(input())
if a < b:
    step = 1
    b += 1
else:
    step = -1
    b -= 1
for i in range(a,b,step):
    print(i)



