class Calculator:
    #def __init__(self,addition,subtraction,multiplication,division):
     #  self.subtraction=subtraction
      #  self.multiplication=multiplication
       # self.division=division

    def addition(self,a,b):
        return a+b
    def subtraction(self,a,b):
        return a-b
    def multiplication(self,a,b):
        return a*b
    def division(self,a,b):
        return a/b

a,b=list(map(int,input("enter 2 numbers:").split()))
add=Calculator.addition(a,b)
