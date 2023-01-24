"""
Day 69 coding Statement : Suppose, we have a class A which is the base class and we have a class B which is derived from class A and we have a class C which is derived from class B, we can access the functions of both class A and class B by creating an object for class C.

Hence, this mechanism is called multi-level inheritance. (B inherits A and C inherits B.)

Create a class called Equilateral which inherits from Isosceles and should have a function such that the output is as given below.

Sample Output

I am an equilateral triangle

I am an isosceles triangle I am a triangle
"""
#Python solution
class Isosceles(object):
    def display1(self):
        print("Iam an isosceles triangle Iam a triangle")
class Equilateral(Isosceles) :
    def display2(self):
        print("I am an equilateral triangle")
tr=Equilateral()
tr.display2()
tr.display1()
