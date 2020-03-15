#A method to find root using bisection methods

class Bisection:
    def __init__(self,Expression,Upper,Lower,Precission):
        self.Expr = ""
        self.Expr = Expression
        self.Upper = Upper
        self.Lower = Lower
        self.pr = 0.1**Precission
    def Function(self,val):
        self.Expr.replace('^' , '**')
        return eval(self.Expr.replace('x',str(val)))

    def CheckRoot(self):
        if self.Function(self.Upper) * self.Function(self.Lower) >= 0:

            return False
        else:
            return True

    def FindRoot(self):
        #if self.CheckRoot():
        #   return
        mid=0
        itr1=0
        #while(self.Function(self.Upper)-self.Function(self.Lower)>self.pr):
        while(itr1<30):
            mid = (self.Upper + self.Lower) / 2
            functionMid=self.Function(mid)
            functionUpper=self.Function(self.Upper)
            functionLower=self.Function(self.Lower)
            if functionLower*functionMid<0:
                self.Upper=mid
            else:
                self.Lower=mid
            itr1=itr1+1
        return mid

ob=Bisection('x**2-5x+6',1,4,5)
root=ob.FindRoot()
print(root)