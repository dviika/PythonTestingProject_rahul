from oopDemo import User

class ChildClass(User):
    childClassVariable = 200

    def __init__(self):
        User.__init__(self, 2,10 )

    def getCompleteData(self):
        return self.childClassVariable + self.age + self.summation()

obj = ChildClass()
print(obj.getCompleteData())
