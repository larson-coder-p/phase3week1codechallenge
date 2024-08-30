##add numbers
def add_numbers(num1, num2):
    return num1 + num2

def is_even(number):
    return number % 2 == 0

#reverse_string
def reverse_string(text):
    return text[::-1]

#count_vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

#calculate_factorial
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial


# Decorator Function
def apply_decorator(func):
    def decorator_func(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return decorator_func

#sort_by_age
def sort_by_age(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: x[1])

#merge-dicts
def merge_dicts(dict1, dict2):
    merged = dict1.copy()  
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value  
        else:
            merged[key] = value  
    return merged

 #Car Class 
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

  
    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")


# Testing add_numbers
print(add_numbers(5, 7)) 
print(add_numbers(-1, 3))  

# Testing is_even
print(is_even(4))  
print(is_even(7)) 

# Testing reverse_string
print(reverse_string("hello")) 
print(reverse_string("Python"))  
# Testing count_vowels
print(count_vowels("hello"))  
print(count_vowels("PYTHON"))  

# Testing calculate_factorial
print(calculate_factorial(5))  
print(calculate_factorial(0))  

# Testing apply_decorator
def sample_function():
    print("Function Executed")

decorated_function = apply_decorator(sample_function)
decorated_function()  
# Testing sort_by_age
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
sorted_people = sort_by_age(people)
print(sorted_people)  

# Testing merge_dicts
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 15, "c": 5, "d": 25}
merged_dict = merge_dicts(dict1, dict2)
print(merged_dict)  

# Testing Car class
my_car = Car("Toyota", "Corolla", 2020)
my_car.display_info()  # Expected output: "Make: Toyota, Model: Corolla, Year: 2020"



