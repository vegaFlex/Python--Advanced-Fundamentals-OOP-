from project.employee import Employee
from project.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."


pers = Teacher()
print(pers.teach())
print(pers.sleep())
print(pers.get_fired())
