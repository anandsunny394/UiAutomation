from NPPractice.constructorexample2 import Example2


class child(Example2):
    child_var=300


    def __init__(self):
        Example2.__init__(self,10,20)

    def summation_child(self):
        var3=500
        sum1 = var3+ child.child_var + self.num + self.sum()
        return sum1


child_obj=child()
print(child_obj.summation_child())