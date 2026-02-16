class Person:
    def __init__(self, name: str, phone_num: int, email: str):
        self.name = name
        self.phone_num = phone_num
        self.email = email

class Student(Person):
    def __init__(self, name, phone_num, email, studentID: int, averge_grade: int):
        super().__init__(name, phone_num, email)
        self.studentID = studentID
        self.averge_grade = averge_grade


    def enlist_for_class():
        pass

class Professor(Person):
    def __init__(self, name, phone_num, email):
        super().__init__(name, phone_num, email)

    def receve_salary():
        pass

class Address:
    def __init__(self, street):
        self.street = street
        
class HomeAddress(Person, Address):
    def __init__(self, name, phone_num, email):
        super().__init__(name, phone_num, email)
        Address.__init__(self, street)
