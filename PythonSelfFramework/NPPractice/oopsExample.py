class sample:
    class_var=100

    def __init__(self):
        print("constructor method")
        
    def method_1(self):
        instance_var=200
        sum=instance_var+sample.class_var
        return sum




obj=sample()
print(obj.method_1())