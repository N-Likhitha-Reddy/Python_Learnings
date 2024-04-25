
class Person:
    def __init__(self, name, age):
        self.person_name = name
        if age >= 0:
            self.__person_age = age
        else:
            print("Age cannot be negative. Setting age to 0.")
            self.__person_age = 0

    def display_info(self):
        print("Name of the person is ", self.person_name)
        print("Age of the person is ", self.__person_age)

    def get_age(self):
        return self.__person_age

    def set_age(self, new_age):
        if new_age >= 0:
            self.__person_age = new_age
        else:
            print("Age cannot be negative.")


person_name = input("Enter name of the person ")
person_age = int(input("Enter valid age of the person "))
person1 = Person(person_name, person_age)
person1.display_info()

print(" ****Using getter method**** ")
print("Current age of the person is :", person1.get_age())


print(" ****Using setter method**** ")
person_age = int(input("Enter age of the person to set "))
person1.set_age(person_age)
person1.display_info()
