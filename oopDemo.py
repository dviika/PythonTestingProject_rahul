#classes are user defined blueprint or prototype
#methods  (sum, multiplication, addition, variables, constant

class User:
    age = 100 #class variable

    def __init__(self, a, b): #default const that will created with class even without creation
        self.first_number = a
        self.second_number = b
        print('I am executing first as method in constructor of class User when the object is created')

    def getData(self):
        print('I am executing as method in class User')

    def summation(self): #self is req when method of the class is created
        return self.first_number + self.second_number + self.age #self.age or User.age
        print('I am executing as method in User')

object_of_the_class0 = User(2,3) #syntax to create an object
object_of_the_class0.getData()
print(object_of_the_class0.summation())
print(object_of_the_class0.age)

object_of_the_class1 = User(4, 5) #syntax to create an object
print(object_of_the_class1.summation())
print(object_of_the_class1.age)