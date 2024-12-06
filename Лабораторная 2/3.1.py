"""nch = [3, 5, 7, 9]
def is_prime(number):
    if number%2 != 0:
        for i in nch:
            if number%i != 0:
                print("True")
                break
    else: print("False")
is_prime(int(input("Введите число: "))) """

def is_prime(num):
    if num < 2:
        return False

    else:
        for i in range(2, num // 2):
            if num % i == 0:
                return False
        return True

# Пример использования функции
number = int(input("Введите число: "))
print(is_prime(number))

