def describe_person(name, age=30):
    return print(f"Имя человека: {name},\nВозраст: {age} лет")
name = input("Введите имя: ")
describe_person(name)
