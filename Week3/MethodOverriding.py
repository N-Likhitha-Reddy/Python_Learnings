

class Person:
    def __init__(self, name, age):
        self.person_name = name
        if age >= 0:
            self.person_age = age
        else:
            print("\n Age cannot be negative. Setting age to 0.")
            self.person_age = 0

    def display_info(self):
        print("Name of the person is ", self.person_name)
        print("Age of the person is ", self.person_age)


class Employee(Person):
    def __init__(self, name, age, id, salary):
        super().__init__(name, age)
        if id >= 0:
            self.employee_id = id
        else:
            print("Employee Id cannot be negative. Setting id to 0.")
            self.employee_id = 0
        self.employee_salary = salary

    def calculate_salary(self):
        return self.employee_salary

    def display_info(self):
        print("\n***Displaying Employee Info***")
        super().display_info()
        print("Id of the employee is ", self.employee_id)
        print("Salary of the employee is ", self.calculate_salary())


def employee_info():
    employee_name = input("Enter name of the employee ")
    employee_age = int(input("Enter age of the employee "))
    employee_id = int(input("Enter id of the employee "))
    employee_salary = float(input("Enter salary of the employee "))
    employee1 = Employee(employee_name, employee_age, employee_id, employee_salary)
    employee1.display_info()


employee_info()