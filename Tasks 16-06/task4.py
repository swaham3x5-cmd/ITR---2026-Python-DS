def add(a,b):
    print(f"Addition is:{a+b}")
def sub(a,b):
    print(f"Subtraction :{a-b}")
def mul(a,b):
    print(f"Multiplication is:{a*b}")
def div(a,b):
    if b==0:
        print("invalid input")
    else:
        print(f"division is:{a/b}")
a=int(input("Enter the first numner:"))
b=int(input("Enter the second number :"))
add(a,b)
sub(a,b)
mul(a,b)
div(a,b)