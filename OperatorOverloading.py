class opOl:
    def __init__(self,value):
        self.value = value

    def __mul__(self,other):
        return opOl(self.value * other.value)

    def __add__(self,other):
        return opOl (self.value + other.value) 
    
    def __str__(self):
        return f'Operator overloaded ended up with: {self.value}'
        #__str__ -  special method  returns string representation of the object.
    
obj11 = opOl(10)
obj22 = opOl(4)
obj33 = opOl(2)

get = (obj11 * obj22)  + obj33
print(get)

