# Program for fast exponentiation in python
# This uses the 2^k-ary binary method for finding the exponent of a number in Olog(n) time.


def multiply(num, exp):
    prod = 1
    while exp > 0:
        if (exp & 1) != 0:
            prod = prod * num
        num = num * num
        exp >>= 1

    return prod


n = int(input("Enter the number to find the exponent of."))
exp = int(input("Enter the power that you find."))
print("Power is ", format(multiply(n, exp)))
