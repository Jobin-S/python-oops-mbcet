from abc import ABC, abstractmethod

# Interface - Employee
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def display_details(self):
        pass

    @staticmethod
    def generate_summary(employees):
        summary = {}
        total_salary = 0
        for employee in employees:
            type_name = type(employee).__name__
            if type_name not in summary:
                summary[type_name] = {'total': 0, 'count': 0}
            summary[type_name]['total'] += employee.calculate_salary()
            summary[type_name]['count'] += 1
            total_salary += employee.calculate_salary()

        for key, value in summary.items():
            print(f"{key}: {value['count']} employees, Total Salary: ${value['total']:.2f}")
        print(f"Total Salary Expenditure: ${total_salary:.2f}")

# Derived Class - Manager
class Manager(Employee):
    def __init__(self, name, age, base_salary, bonus):
        self.name = name
        self.age = age
        self.base_salary = base_salary
        self.bonus = bonus

    def calculate_salary(self):
        if self.base_salary < 0 or self.bonus < 0:
            raise ValueError("Salary and bonus must be non-negative.")
        return self.base_salary + self.bonus

    def display_details(self):
        print(f"Manager Name: {self.name}, Age: {self.age}, Salary: ${self.calculate_salary():.2f}")

# Derived Class - Developer
class Developer(Employee):
    def __init__(self, name, age, base_salary, project_count):
        self.name = name
        self.age = age
        self.base_salary = base_salary
        self.project_count = project_count

    def calculate_salary(self):
        if self.base_salary < 0 or self.project_count < 0:
            raise ValueError("Salary and project count must be non-negative.")
        return self.base_salary + 1000 * self.project_count  # Assuming bonus of $1000 per project

    def display_details(self):
        print(f"Developer Name: {self.name}, Age: {self.age}, Salary: ${self.calculate_salary():.2f}")

# Derived Class - Intern
class Intern(Employee):
    def __init__(self, name, age, hourly_rate, hours_worked):
        self.name = name
        self.age = age
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        if self.hourly_rate < 0 or self.hours_worked < 0:
            raise ValueError("Hourly rate and hours worked must be non-negative.")
        return self.hourly_rate * self.hours_worked

    def display_details(self):
        print(f"Intern Name: {self.name}, Age: {self.age}, Salary: ${self.calculate_salary():.2f}")

# Example usage
employees = [
    Manager("John Doe", 45, 50000, 7000),
    Developer("Jane Smith", 33, 80000, 5),
    Intern("Alice Johnson", 22, 15, 160)
]

# Display details and generate summary
for employee in employees:
    employee.display_details()
Employee.generate_summary(employees)
