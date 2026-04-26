class A:
    clName="A"

    def __init__(self): 
        self.name="srinu" 
        print("a class init method")

    def height_A(self): 
        self.height=5.7
         
        print(self.height)

    def land_A(self):
        self.land="8acre"
        print(self.land)    

class B(A):
    clName="B"

    def __init__(self):
        print("b class init method") 

    def acquireChars(self):
        print("acquireChars method")  
        print(super().clName) 
        super().height_A()  
        super().height_A() 
        super().land_A()

o=B()    
print(o.clName) 
o.acquireChars()