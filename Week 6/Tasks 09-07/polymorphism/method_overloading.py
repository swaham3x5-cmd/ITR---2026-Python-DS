class example:
    def add(self, a,b):
        x = a+b
        return x

    def add(self, a,b,c):
        x = a+b+c
        return x
    
obj = example()    
print(f"{obj.add(10,20)}")
print(f"{obj.add(1,2,2)}")