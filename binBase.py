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
    while fractionalBits > 0:
        if fractionalBits % 2 == 1:
            ans *= base

        base *= base
        fractionalBits //= 2

    return ans

def convHelper(num):
    """
    The function `convHelper` converts a given number into its binary representation, including handling
    negative and floating-point numbers.
    
    :param num: The `convHelper` function you provided seems to be converting a given number into its
    binary representation. The function first checks if the number is negative or a float, then performs
    the conversion accordingly
    :return: The function `convHelper` is converting a given number into its binary representation. If
    the input number is a float, it first converts it to an integer by multiplying it with a power of 2,
    then proceeds to convert the absolute value of the number to binary. If the input number is an
    integer, it directly converts the absolute value to binary.
    """
    isNeg = True if num < 0 else False
    isFloat = isinstance(num, float)
    if isFloat:
        powBase = my_pow(2, 8)
        num = int(abs(num*powBase)) if isNeg else int(num*powBase)
    else:
        num = abs(num) if num < 0 else num

    binBase = ""
    while num > 0:
        rem = num % 2
        binBase = f"{binBase}{rem}"
        num //= 2

    c, temp = len(binBase)-1, ""
    while c >= 0:
        if isFloat and c == 7:
            temp = f"{temp}."

        temp = f"{temp}{binBase[c]}"
        c -= 1
    
    binBase = f"0.{temp.zfill(8)}" if len(temp) <= 8 and isFloat else temp
    if isNeg:
        binBase = f"-{binBase}"

    return binBase

def numto_Bin(num=None):
    """
    The function `numto_Bin` converts a given number to its binary representation.
    
    :param num: The given code defines a function `numto_Bin` that converts a decimal number to its
    binary representation. The function checks if a number has been provided, and if not, it prints a
    message and returns `None`. It then checks if the number is 0 or 1 and returns the
    :return: The function `numto_Bin` is returning the binary representation of the input number
    `num`. If `num` is not provided, it will print "No number has been provided!" and return `None`. If
    the input number is 0 or 1, it will return the number itself as a string. Otherwise, it will call
    the `convHelper` function to convert the number to
    """
    if num is None:
        print("No number has been provided!")
        return
    
    binBase = ""
    if num == 0 or num == 1:
        return f"{int(num)}"
    else:
        binBase = convHelper(num)

    return binBase

if __name__ == "__main__":
    res = numto_Bin(2)
    print(f"{res}\n{type(res)}")