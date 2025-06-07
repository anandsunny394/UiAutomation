class Example2:
    num=200

    def __init__(self,a,b):
        self.firstNo=a
        self.secondNo=b


    def sum(self):
        return self.firstNo+self.secondNo+Example2.num

obj1=Example2(10,20)
print(obj1.sum())

obj2=Example2(30,40)
print(obj2.sum())




