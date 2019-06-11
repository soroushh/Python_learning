class Lis:
    def __init__(self,list):
        self.list = list

    def add_name(self,object):
        self.list.append(object)


class Person:
    def __init__(self,name,family):
        self.name = name
        self.family = family

    def full_name(self):
        return(self.name + " "+ self.family)

    def go_to_list(self,list):
        list.add_name(self)


person = Person("soroush","khosravi")

lis = Lis([])

person.go_to_list(lis)

print(lis.list[0].name)

print(lis.list[0].family)
