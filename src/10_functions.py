# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE


def is_even(num): 2


print(num % 2 == 0)


is_even(2)
is_even(3)

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
if (num % 2) == 0:
    print("{0} is Even".format(num))
else:
    print("{0} is Odd".format(num))
