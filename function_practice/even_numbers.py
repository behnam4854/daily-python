

# Generate a Python list of all the even numbers between 4 to 30


def even_numbers(start, end):
    """checking whether the number is even or not"""
    even_list=[]

    for i in range(start, end):
        if i%2==0:
            even_list.append(i)
        else:
            pass
    return even_list

print(even_numbers(4,30))