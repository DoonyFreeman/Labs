with open("user_input.txt", "a") as file:
    text = input("Введите текст: ")
    file.write(text + " ")
