

# Find the largest item from a given list

x = [4, 6, 8, 24, 12, 2,26]


def find_the_largest(x):
    
    if len(x) == 1:
        return x[0]
    
    for i in range(len(x)-1):
        if x[i] < x[i+1]:
            larget = x[i+1]
        else:
            continue
    return larget
 
print("The hardest way possible : " + str(find_the_largest(x)))


# or simply you can use
print("The super duper easy way : " + str(max(x)))


