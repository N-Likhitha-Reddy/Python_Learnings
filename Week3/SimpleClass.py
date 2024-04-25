
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


person_name = input("Enter name of the person ")
person_age = int(input("Enter valid age of the person "))
person1 = Person(person_name, person_age)
person1.display_info()

