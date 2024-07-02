# Object-Oriented Programming Exercises in Python

## Question 1: Bank Account System with Inheritance

### Task

Create a Python class called `BankAccount` which represents a bank account, having as attributes:

1. `accountNumber` (numeric type)
2. `name` (name of the account owner as string type)
3. `balance`

#### Requirements

- Create a constructor with parameters: `accountNumber`, `name`, `balance`.
- Create a `Deposit()` method which manages the deposit actions.
- Create a `Withdrawal()` method which manages withdrawals actions.
- Create a `bankFees()` method to apply the bank fees with a percentage of 5% of the balance account.
- Create a `display()` method to display account details.

### Additional Activity for Question 1

- Create a `Person` Class.
- Create a `UPI` class.
- Create hierarchy inheritance (`Person > BankAccount > UPI`).
- Override `display` function with message and value concatenation.
- Create a method for UPI transfer that accepts a value (`to: Person obj, value:int`).

## Question 2: Class Inheritance

### Given Task

Create a `Bus` child class that inherits from the `Vehicle` class. The default fare charge of any vehicle is seating capacity * 100. If the vehicle is a Bus instance, we need to add an extra 10% on full fare as a maintenance charge.

#### Requirements

- Bus seating capacity is 50, so the final fare amount should be 5550.
- Override the `fare()` method of the `Vehicle` class in the `Bus` class.
- Use the provided code for your parent `Vehicle` class.
- Access the parent class from inside a method of the child class.

## Question 3: Multi-level Inheritance and Method Overriding

### Task Description

Create a system that models a digital library containing different types of media, such as books, magazines, and audiobooks. Each type of media shares common traits but also has unique characteristics.

#### Requirements

- Base Class - `Media`: Attributes include `title`, `creator`, `publish_year`, `genre`; and a method `display_info()`.
- Derived Classes - `Book`, `Magazine`, `Audiobook` with specific attributes and overridden `display_info()` method.
- Implement a search method in the base class for filtering objects based on attributes like `genre` or `creator`.

### Additional Challenge

Implement a method in the base class that allows filtering objects based on attribute values.

## Question 4: Implement an Interface and Exception Handling

### Task Description

Develop a system to manage employee records for a company handling different types of employees such as managers, developers, and interns.

#### Requirements

- Define an interface `Employee` with abstract methods `calculate_salary()` and `display_details()`.
- Derived Classes - `Manager`, `Developer`, `Intern` implement the `Employee` interface with specific attributes.
- Use Python's `abc` module to enforce the implementation of interface methods.
- Implement exception handling for errors such as invalid attribute values.

### Additional Challenge

Add a method in the base interface that generates a summary report of all employee types and their total salary expenditure.

This exercise will test your ability to design a system using interfaces, implement classes based on these interfaces, and handle potential runtime errors using exception handling in Python.
