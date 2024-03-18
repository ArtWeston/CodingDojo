num1 = 42         #variable declaration
num2 = 2.3        #variable declaration
boolean = True       #Boolean
string = 'Hello World'       #Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']       #List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}       #Dictionary
fruit = ('blueberry', 'strawberry', 'banana')       #List
print(type(fruit))       #List
print(pizza_toppings[1])       #Strings
pizza_toppings.append('Mushrooms')       #
print(person['name'])       #Strings
person['name'] = 'George'       #Strings
person['eye_color'] = 'blue'       #Strings
print(fruit[2])       #Strings

if num1 > 45:       #conditional if
    print("It's greater")       #
else:       #conditional else
    print("It's lower")       #

if len(string) < 5:       #conditional
    print("It's a short word!")       #
elif len(string) > 15:       #conditional
    print("It's a long word!")       #
else:
    print("Just right!")       #conditional

for x in range(5):       #for loop
    print(x)
for x in range(2,5):       #for loop
    print(x)
for x in range(2,10,3):       #for loop
    print(x)
x = 0
while(x < 5):       #while loop
    print(x)
    x += 1

pizza_toppings.pop()       #add value
pizza_toppings.pop(1)       #add value

print(person)       #Strings
person.pop('eye_color')       #add value
print(person)       #Strings

for topping in pizza_toppings:       #for loop
    if topping == 'Pepperoni':       #conditional
        continue
    print('After 1st if statement')       #Strings
    if topping == 'Olives':       #conditional
        break

def print_hello_ten_times():       #Strings
    for num in range(10):       #for loop
        print('Hello')

print_hello_ten_times()       #Strings

def print_hello_x_times(x):       #Strings
    for num in range(x):       #for loop
        print('Hello')       #Strings

print_hello_x_times(4)       #Strings

def print_hello_x_or_ten_times(x = 10):       #Strings
    for num in range(x):       #for loop
        print('Hello')       #Strings

print_hello_x_or_ten_times()       #Strings
print_hello_x_or_ten_times(4)       #Strings


"""    #Comment Multiple Lines
Bonus section
"""

# print(num3)       #NameError: name <variable name> is not defined
# num3 = 72       #
# fruit[0] = 'cranberry'       #TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team'])       #KeyError: 'favorite_team'
# print(pizza_toppings[7])       #IndexError: list index out of range
# print(boolean)       #
# fruit.append('raspberry')       #AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1)       #AttributeError: 'tuple' object has no attribute 'pop'