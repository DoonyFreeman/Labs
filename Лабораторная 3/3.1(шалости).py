def fuu():                                                                                               #ФУНКЦИЯ ЧТЕНИЯ ФАЙЛА (ОБЩАЯ ФУНКЦИЯ)

    def ans(answer):                                                                                     #ПРИНЯТИЕ РЕШЕНИЯ
        if answer == "1":
            return fuu()                                                                                 #ВЫЗОВ ОБЩЕЙ ФУНКЦИИ
        elif answer == "2":
            print("Спасибо за пользование файлохранилищем, bie!")                                        #ПРОЩАНИЕ И ЗАВЕРШЕНИЕ
        else:
            answer = input("Введите 1 или 2!: ")
            ans(answer)                                                                                   #ВЫЗЫВАЕМ ПРИНЯТИЕ РЕШЕНИЯ



    try:
        name = input("\n\n-----------------------------------\n\nВведите название тектового файла: ")
        with open(str(name), "r+") as file:                                                               #ОТКРЫВАЕМ И ЧИТАЕМ ФАЙЛ
            content = file.read()
            print("\nСодержимое файла:", content,"\n\nОткрыть ещё файл?\n1 - Да, 2 - Нет")
            answer = input("Введите 1 или 2: ")
            ans(answer)                                                                                   #ВЫЗЫВАЕМ ПРИНЯТИЕ РЕШЕНИЯ

    except FileNotFoundError:                                                                             #ИСКЛЮЧЕНИЕ И ВЫЗОВ ОБЩЕЙ ФУНКЦИИ FUU()
        print("Файл не найден, введите название файла корректно!")
        return fuu()

fuu()
