class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Technician(Employee):
    def __init__(self, name, id, specialization):
        super().__init__(name, id)
        self.specialization = specialization
def perform_maintenance(self):
    return f"Техник {self.name} выполняет техническое обслуживание в области {self.specialization}"

class Manager(Employee):
    def __init__(self, name, id, department):
        super().__init__(name, id)
        self.department = department

class TechManager(Manager):
    def __init__(self, name, id, department, specialization):
        super().__init__(name, id, department)
        self.specialization = specialization
        self.employees = []
    def manage_project(self):
        return f"Менеджер {self.name} управляет проектом в {self.department}"
    def perform_maintenance(self):
        return f"Техник {self.name} выполняет техническое обслуживание в области {self.specialization}"
    def add_employee(self, employee):
        self.employees.append(employee)
    def get_team_info(self):
        return "\n".join(f"{employee.name} (ID: {employee.id})" for employee in self.employees)


tech1 = Technician("Иван", 1,"Электроника")
tech2 = Technician("Мария", 2, "Механика")
# Создаем менеджера
manager = TechManager("Сергей",3, "Технический отдел", "Обслуживание")
# Добавляем техников в команду менеджера
manager.add_employee(tech1)
manager.add_employee(tech2)
# Тестируем методы
print(manager.manage_project()) # Выводит информацию о проекте
print(manager.perform_maintenance()) # Выводит информацию о техническом обслуживании
print(manager.get_team_info()) # Выводит информацию о команде