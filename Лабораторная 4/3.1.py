

import modalls
question = int(input("1. - умножение\n2. - деление\n"))
if question == 1:
    print(modalls.multip(int(input("Первое число: ")), int(input("Второе число: "))))
elif question == 2:
    print(modalls.add(int(input("Первое число:")), int(input("Второе число:"))))