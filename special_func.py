class Student:
    def __init__(self, name, total_mark):
        self.name = name
        self.total_mark = total_mark

    def __add__(self, other):
        return self.total_mark + other.total_mark

jobin = Student("Jobin Selvanose", 58)
nikhil = Student("Nikhil", 69)

print(jobin.total_mark + nikhil.total_mark)
print(jobin + nikhil)


class Name:
    def __init__(self, name):
        self.name = name;

    def __add__(self, other):
        return self.name + other.name

first_name = Name("Jobin")
last_name = Name("Selvanose")
print(first_name + last_name)
print(first_name)
