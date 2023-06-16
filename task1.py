"""Exercise(OOP - Inheritance - MRO):
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
Explain the order of the output based on the method
 resolution order (MRO) and activation sequences."""

 # Solution


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

d = D()


"""
The expected output when an instance of class D is created is as follows:

Initializing class D
Initializing class B
Initializing class C
Initializing class A

Explanation:
When an instance of class D is created, the __init__ method of class D is invoked first.
Within the __init__ method of class D, the print("Initializing class D") statement is executed,
 printing "Initializing class D" to the console.
The super().__init__() statement in the __init__ method of class D calls
 the __init__ method of the next class in the method resolution order (MRO), which is class B.
Consequently, the __init__ method of class B is invoked.
Within the __init__ method of class B, the print("Initializing class B")
 statement is executed, printing "Initializing class B" to the console.
The super().__init__() statement in the __init__ method of class B calls
 the __init__ method of the next class in the MRO, which is class C.
Hence, the __init__ method of class C is executed.
Within the __init__ method of class C, the print("Initializing class C")
 statement is executed, printing "Initializing class C" to the console.
The super().__init__() statement in the __init__ method of class C calls
 the __init__ method of the next class in the MRO, which is class A.
Therefore, the __init__ method of class A is called.
Inside the __init__ method of class A, the print("Initializing class A")
 statement is executed, printing "Initializing class A" to the console.
After the super().__init__() statement in the __init__ method of class A,
 there are no more classes in the MRO to call, and the initialization process is complete.
The order of the output is based on the method resolution order (MRO)
 and the activation sequences. In this case, the MRO follows
 a depth-first left-to-right order. When resolving the method chain,
it starts from the leftmost parent class (B) and follows
 the inheritance hierarchy, eventually reaching the base class (A).
This order ensures that each class's __init__ method is called exactly
 once and in the correct order."""