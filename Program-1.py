# Problem-1: Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
# Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
# Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string

class Calculator:
    
    def __init__(self, num1, num2, operation):
        self.num1= num1
        self.num2 = num2
        self.operation = operation.lower()
    
    
    def calculate(self):
        if self.operation == "add":
            return self.num1 + self.num2
        
        elif self.operation == "subtract":
            return self.num1 - self.num2
        
        elif self.operation == "multiply":
            return self.num1 * self.num2
        
        elif self.operation == "divide":
            if self.num2 == 0:
                return  "zero with division is not possible !"
            return self.num1 / self.num2
        
        else:
            return "enter the valid and correct operation as same as give refrence of the operations !"
    

num1 = float(input("enter the first number :"))
num2 = float(input("enter the second number :"))
print("(add, subtract, multiply,divide):")
operation = str(input("enter the operation in the above operations: "))

obj = Calculator(num1, num2, operation)
res = obj.calculate()
print("the result :", res)



###################################################################
#### Output :
# enter the first number :3
# enter the second number :6
# (add, subtract, multiply,divide):
# enter the operation in the above operations: multiply
# the result : 18.0
