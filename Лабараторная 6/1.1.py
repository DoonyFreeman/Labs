class UserAccount:
    def __init__(self, username, email ,password):
        self.username = username
        self.email = email
        self.password = password
        print(f"Объект создан: \n Username: {username} \nemail: {email} \npassword:{password}")
    def set_password(self, new_password):
        self.password = new_password
        pasw = ""
        for a in range(len(self.password)):
            pasw = pasw + "*"
        print(f"пароль был изменён: {pasw}")
    def check_password(self, password):
        print(self.password == password)
user1 = UserAccount("Shah", "22888@gmail.com", "ZZZZ")
user1.set_password("VOO")
user1.check_password(input("Пароль сюды введи!:"))