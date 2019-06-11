class Number:
    def __init__(self,amount):
        self.amount = amount

    def devisibles(self,devs = [], counter = 1):
        while counter <= self.amount:
            if self.amount % counter == 0 :
                devs.append(counter)
            counter += 1
        return(devs)

    def prime(self):
        if len(self.devisibles()) == 2:
            return(True)
        return(False)

num = Number(13)

print(num.prime())
