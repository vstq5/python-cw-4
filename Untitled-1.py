def my_name():
    print("my name is ali")

my_name()

def my_meal1(food , drinks):
    print(f"i would like to eat {food} while drinking {drinks}")
my_meal1("pizza" , "cola")
def cube(number):
    return number ** 3
print(cube(3))
def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False
result1 = by_three(6)
print(result1)
result2 = by_three(7)
print(result2)

