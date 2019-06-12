class Person:
    def __init__(self,name, family):
        self.name = name
        self.family = family

    def full_name(self):
        return(self.name + " "+ self.family)

class Student(Person):
    def __init__(self, fname , lname , year_of_birth):
        Person.__init__(self,fname, lname)
        self.year_of_birth = year_of_birth

    def show_year_of_birth(self):
        return(self.year_of_birth)
person = Person("soroush","khosravi")
print(person.full_name())

student = Student("farnaz","ostovari",1988)

print(student.full_name())

print(student.show_year_of_birth())
