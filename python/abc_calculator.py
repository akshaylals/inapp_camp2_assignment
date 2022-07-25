# ABC Assignment -  Modificaiton of Calculator
# 
# Modify the previously did calculator program
# * Create an Abstract base class 'Calculate'
# * Then inheriting from it, create CalcSum, CalcDiff,
#   CalcProd, CalcQuo for basic calculations
# * Make sure to validate for numbers in the setter method 


from abc import ABC, abstractmethod


class Calculate(ABC):
    @abstractmethod
    def calculate(self):
        pass

    @property
    def num1(self):
        return self.__num1
    
    @property
    def num2(self):
        return self.__num2
    
    @num1.setter
    def num1(self, num):
        if isinstance(num, int) or isinstance(num, float):
            self.__num1 = num
        else:
            print('Invalid value')
            raise Exception
    
    @num2.setter
    def num2(self, num):
        if isinstance(num, int) or isinstance(num, float):
            self.__num2 = num
        else:
            print('Invalid value')
            raise Exception
    

class CalcSum(Calculate):
    def calculate(self):
        return self.num1 + self.num2


class CalcDiff(Calculate):
    def calculate(self):
        return self.num1 - self.num2


class CalcProd(Calculate):
    def calculate(self):
        return self.num1 * self.num2


class CalcQuo(Calculate):
    def calculate(self):
        return self.num1 // self.num2
        
    @Calculate.num2.setter
    def num2(self, num):
        if num == 0:
            raise Exception
        else:
            Calculate.num2.fset(self, num)
    

class Utils:
    @staticmethod
    def getInt(*msg):
        while(True):
            try:
                value = int(input(*msg))
                return value
            except:
                print('Invalid input')

    @staticmethod
    def getFloat(*msg):
        while(True):
            try:
                value = float(input(*msg))
                return value
            except:
                print('Invalid input')


ops = {
    1: ('Add', CalcSum),
    2: ('Subtract', CalcDiff),
    3: ('Multiply', CalcProd),
    4: ('Divide', CalcQuo)
}


while(True):
    opt = Utils.getInt('''
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Exit
    > ''')
    if not (1 <= opt <= 5):
        print('Invalid input')
        continue
    if opt == 5:
        break
    
    op, Cls = ops[opt]
    obj = Cls()
    obj.num1 = Utils.getFloat('Num1: ')
    while(True):
        try:
            obj.num2 = Utils.getFloat('Num2: ')
            break
        except:
            print("Cannot be zero")

    print(op, obj.calculate())