# Create a class called Calculator
# * While creating the object pass two numbers into it
# * Then call object.add(), multiply(), divide() methods to get the result

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        return self.num1 / self.num2
    
obj = Calculator(4, 5)
print('Add:', obj.add())
print('Multiply:', obj.multiply())
print('Divide:', obj.divide())