
class Person:
    def __init__(self, name, age):
        self.person_name = name
        if age >= 0:
            self.person_age = age
        else:
            print("Age cannot be negative. Setting age to 0.")
            self.person_age = 0

    def display_info(self):
        print("Name of the person is ", self.person_name)
        print("Age of the person is ", self.person_age)


class Employee(Person):
    def __init__(self,name,age,id):
        self.employee_name = name
        if age >= 0:
            self.employee_age = age
        else:
            print("\nEmployee Age cannot be negative. Setting age to 0.")
            self.employee_age = 0
        if id >= 0:
            self.employee_id = id
        else:
            print("Employee Id cannot be negative. Setting id to 0.")
            self.employee_id = 0


    def display_info(self):
        print("\n***Displaying Employee Info***")
        print("Name of the employee is ", self.employee_name)
        print("Age of the employee is ", self.employee_age)
        print("Id of the employee is ", self.employee_id)


def employee_info():
    employee_name = input("Enter name of the employee ")
    employee_age = int(input("Enter valid age of the employee "))
    employee_id = int(input("Enter valid id of the employee "))
    employee1 = Employee(employee_name, employee_age, employee_id)
    employee1.display_info()


employee_info()