def my_pow(base, fractionalBits):
    """
    The function `my_pow` calculates the power of a given base with a specified number of fractional
    bits using a binary exponentiation algorithm.
    
    :param base: The `base` parameter in the `my_pow` function represents the base number that will be
    raised to a power. This is the number that will be multiplied by itself a certain number of times
    based on the `fractionalBits` parameter
    :param fractionalBits: The `fractionalBits` parameter in the `my_pow` function represents the number
    of fractional bits to consider when calculating the power of a given base. It is used in the
    function to determine how many iterations of squaring the base are needed to calculate the final
    result
    :return: The function `my_pow` returns the result of raising the `base` to the power of
    `fractionalBits`.
    """
    ans = 1
    while(fractionalBits > 0):
        if fractionalBits % 2 == 1:
            ans *= base

        base *= base
        fractionalBits //= 2

    return ans

def convHelper(num):
    """
    This Python function converts a decimal number to its binary representation, including handling
    floating-point numbers.
    
    :param num: It looks like the code you provided is a helper function for converting a decimal number
    to its binary representation. The `convHelper` function takes a number as input and converts it to
    binary
    :return: The function `convHelper` is converting a given number into its binary representation. If
    the input number is a float, it first scales the number and then converts it to binary. The binary
    representation is then formatted with a decimal point if the input was a float. Finally, the
    function returns the binary representation of the input number. If the input number was negative,
    the binary representation is preceded by a
    """
    binBase = ""

    if isinstance(num, float):
        powBase = my_pow(2, 8)
        newNum = int(abs(num*powBase)) if num < 0 else int(num*powBase)
    else:
        newNum = abs(num) if num < 0 else num

    while newNum > 0:
        rem = newNum % 2
        binBase = f"{binBase}{rem}"
        newNum //= 2

    c, temp = len(binBase)-1, ""
    while c >= 0:
        if isinstance(num, float) and c == 7:
            temp = f"{temp}."
        temp = f"{temp}{binBase[c]}"
        c -= 1
    
    binBase = temp
    if num < 0:
        return f"-{binBase}"
    else:
        return binBase

def numto_Binary(num=None):
    """
    The function `numto_Binary` converts a given number to its binary representation.
    
    :param num: The given code defines a function `numto_Binary` that converts a decimal number to its
    binary representation. The function checks if a number has been provided, and if not, it prints a
    message and returns `None`. It then checks if the number is 0 or 1 and returns the
    :return: The function `numto_Binary` is returning the binary representation of the input number
    `num`. If `num` is not provided, it will print "No number has been provided!" and return `None`. If
    the input number is 0 or 1, it will return the number itself as a string. Otherwise, it will call
    the `convHelper` function to convert the number to
    """
    if num is None:
        print("No number has been provided!")
        return
    
    binBase = ""
    if int(num) == 0 or int(num) == 1:
        return f"{num}"
    else:
        binBase = convHelper(num)

    return binBase

if __name__ == "__main__":
    res = numto_Binary(43.167)
    print(f"{res}\n{type(res)}")