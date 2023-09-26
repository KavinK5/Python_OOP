class One:
    def __init__(self,prOne):
      
        self.prOne = prOne

class Two(One):
    def __init__(self,prTwo,prOne):
      
        super().__init__(prOne)
        self.prTwo = prTwo

myObj1 = Two(5,88)

print(myObj1.prOne)
print(myObj1.prTwo)
