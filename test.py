numbers = [1,2,3,4,5]

squares = [num*num for num in numbers]

print(squares)

squares = []

for num in numbers:
    squares.append(num * num)

print(squares)    

evens = [num for num in numbers if num % 2 == 0]
print(evens)

names = ["carl", "jenny", "milani","nina", "riku", "boy"]

c_names = [name.upper() for name in names if name.startswith("c")]
print(c_names)

my_dict = {"a": 1, "b":2}

my_dict["c"] = 3

print(my_dict)

for x in my_dict:
    print(f'{x} is they key and {my_dict[x]} is the value.')
   