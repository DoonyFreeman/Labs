try:
    name = input()
    with open(str(name), "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Файл не найден, введите название файла корректно!")
    