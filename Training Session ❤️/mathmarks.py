class Marks:
    def __init__(self,name,mark):
        self.__mark = mark
        self.name=name
        #self.mark=mark
    def getmark(self,mark):
        return self.__mark
    def setmark(self,mark):
        self.mark=marks

m1=Marks("juck",67)
m2=Marks("mahesh",78)
print(Marks.getmark(m1))
m1.getmark()