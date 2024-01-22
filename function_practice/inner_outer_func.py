

# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it


def func_outer(a, b):
    """simple function that receive a and b"""

    def inner():
        """addintion of passed arguments"""
        return a+b
    
    return inner()

print("the result is : " + str(func_outer(8, 11)))