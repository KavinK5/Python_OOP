class MethOvrl():
    def func1(x = None,y = None,z = None):
        if x != None and z != None and y != None:
            return 'Triple Parameter'
        
        elif x != None and y != None:
            return 'Double Parameter'
        
        elif x != None:
            return 'The Single parameter'
        
obj2 = MethOvrl
gt = obj2.func1('K','A','v')
print(gt)