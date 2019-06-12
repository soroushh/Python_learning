class Person :
    def __init__ (self, name, family):
        self.name = name
        self.family = family
    def full_name(self):
        return("The full name is "+ self.name +" "+ self.family)

soroush = Person("soroush","khosravi")

print(soroush.full_name())

print(soroush.name)
