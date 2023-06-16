# Exercise(OOP - Inheritance - MRO):

Consider the following classes and their inheritance hierarchy:
class A:
    def __init__(self):
        print("Initializing class A")
        super().__init__()

class B(A):
    def __init__(self):
        print("Initializing class B")
        super().__init__()

class C(A):
    def __init__(self):
        print("Initializing class C")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("Initializing class D")
        super().__init__()
Write down the expected output when an instance of class D is created.
Explain the order of the output based on the method resolution order
(MRO) and activation sequences.