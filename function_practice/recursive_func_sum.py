


# Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
# A recursive function is a function that calls itself again and again.

# Expected Output:
# 55


def sum_recersive(number):
    """recersive function to calculate the sum of given numbers"""
    if number:
        return number + sum_recersive(number-1)
    else:
        return 0
    

print(sum_recersive(995))