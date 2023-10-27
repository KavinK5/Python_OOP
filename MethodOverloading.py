class Calculator:
    def addT(self,pr1,pr2 = 0,pr3 = 0):
        return pr1 + pr2 + pr3
    
obj2 = Calculator()

rec = obj2.addT(9,8,9)
rec


'''
class clName:
    def calcFunc(self,pr1 = None, pr2 = None, pr3 = None):
        if pr1 != None and pr2 != None and pr3 != None:
            return 'First'

        elif pr1 != None and pr2 != None:
            return 'Second'
        
        elif pr1 != None:
            return 'Third'
   
obj = clName()  

st =  obj.calcFunc(2,8,6)
st2 = obj.calcFunc(2)
st3 = obj.calcFunc(2,4)

print(st,st2,st3)
'''
