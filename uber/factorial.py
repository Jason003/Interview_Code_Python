# Python program to compute factorial
# of big numbers

# This function finds factorial of large
# numbers and prints them
def factorial(n):
    res = [None] * 500
    # Initialize result
    res[0] = 1
    res_size = 1

    # Apply simple factorial formula
    # n! = 1 * 2 * 3 * 4...*n
    x = 2
    while x <= n:
        res_size = multiply(x, res, res_size)
        x = x + 1

    s = ''
    for i in range(res_size - 1, -1, -1):
        s += str(res[i])
    return s


# This function multiplies x with the number
# represented by res[]. res_size is size of res[]
# or number of digits in the number represented
# by res[]. This function uses simple school
# mathematics for multiplication. This function
# may value of res_size and returns the new value
# of res_size
def multiply(x, res, res_size):
    carry = 0  # Initialize carry

    # One by one multiply n with individual
    # digits of res[]
    i = 0
    while i < res_size:
        prod = res[i] * x + carry
        res[i] = prod % 10  # Store last digit of
        # 'prod' in res[]
        carry = prod / 10  # Put rest in carry
        i = i + 1

    # Put carry in res and increase result size
    while carry:
        res[res_size] = carry % 10
        carry = carry / 10
        res_size = res_size + 1

    return res_size


# Driver program
print(factorial(15))

# This code is contributed by Nikita Tiwari.