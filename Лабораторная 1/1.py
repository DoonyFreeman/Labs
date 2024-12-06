a = int(input("Ведите число: "))
count = 0
if a>0:
    while count!=a:
        count+=1
        print(count)

elif a<0:
    while count!=a:
        count-=1
        print(count)
else:
    print("Ноль?, ну вот 0")