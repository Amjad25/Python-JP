# class 12 all about S.O.L.I.D Principles

# S - Single Responsibility Principle (SRP)
     # A class should have one, and only one, reason to change.
        # A class should have only one reason to change.
        # A class should have only one responsibility.
        # A class should have only one job to do.
        
# O - Open/Closed Principle (OCP)
    # A class should be open for extension, but closed for modification.
        # A class should be open for extension, but closed for modification.
        # A class should be open for adding new functionality.
        # A class should be closed for changing existing functionality.
    # Solution: Use Inheritance
        # Create a base class that defines the operations that can be performed on the data.
        # Create a derived class for each variation of the data.
        # The client creates an object of the derived class that they need.
        # The client uses the base class to define the operations that can be performed on the data.
        # The client uses the derived class to define the variations of the data.

# L - Liskov Substitution Principle (LSP)
    # Objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program.
        # Objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program.
        # Subtypes must be substitutable for their base types.
        # Derived classes must be substitutable for their base classes.
    # Solution: to do LSP correctly
        # The derived class should not override the base class methods.
        # The derived class should not hide the base class methods.
        # The derived class should not change the base class methods.
        # The derived class should not change the base class method signatures.
        # The derived class should not change the base class method return types.
    # example
        # class Bird:
    



# I - Interface Segregation Principle (ISP)
    # A client should never be forced to implement an interface that it doesn't use or clients shouldn't be forced to depend on methods they do not use.
        # A client should never be forced to implement an interface that it doesn't use.
        # Clients shouldn't be forced to depend on methods they do not use.
        # Many client-specific interfaces are better than one general-purpose interface.

# D - Dependency Inversion Principle (DIP)
    # High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions.
        # High-level modules should not depend on low-level modules.
        # Both should depend on abstractions.
        # Abstractions should not depend on details.
        # Details should depend on abstractions.
    # Solution: Use Dependency Injection
        # Create an interface that defines the operations that can be performed on the data.
        # Create a class that implements the interface.
        # The client creates an object of the class that implements the interface.
        # The client uses the interface to define the operations that can be performed on the data.
        # The client uses the object of the class that implements the interface to perform the operations on the data.

