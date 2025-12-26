def my_pow(base, fractionalBits):
    """
    The function `my_pow` calculates the power of a given base with a specified number of fractional
    bits using a bitwise approach.
    
    :param base: The `base` parameter in the `my_pow` function represents the base number that will be
    raised to a power
    :param fractionalBits: The `fractionalBits` parameter in the `my_pow` function represents the number
    of fractional bits to consider when calculating the power of a given base. It is used in the
    function to determine how many iterations are needed to calculate the result accurately with the
    specified precision
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
    The function convHelper converts a given number into its octal representation.
    
    :param num: It looks like the code you provided is a Python function that converts a number to its
    octal representation. The function seems to handle both integer and floating-point numbers
    :return: The function `convHelper` is converting a given number into its octal representation. The
    octal representation is being returned as a string. If the input number is negative, the octal
    representation will have a negative sign at the beginning. If the input number is a float, the octal
    representation will have a decimal point at the appropriate position.
    """
    isNeg = True if num < 0 else False
    isFloat = isinstance(num, float)
    if isinstance(num, float):
        powBase = my_pow(8, 8)
        num = int(abs(num * powBase)) if isNeg else int(num * powBase)
    else:
        num = abs(num) if isNeg else num
    
    octBase = ""
    while num > 0:
        rem = num % 8
        octBase = f"{octBase}{rem}"
        num //=8

    c, temp = len(octBase) - 1, ""
    while c >= 0:
        if c == 7:
            temp = f"{temp}."
        
        temp = f"{temp}{octBase[c]}"
        c -= 1

    octBase = f"0.{temp.zfill(8)}" if len(temp) <= 8 and isFloat else temp

    if isNeg:
        octBase = f"-{octBase}"

    return octBase

def numto_Oct(num=None):
    """
    The function `numto_Oct` converts a given number to its octal representation.
    
    :param num: The `numto_Oct` function you provided seems to be a Python function that converts a
    given number to its octal representation. However, the `convHelper` function is not defined in the
    code snippet you provided
    :return: The function `numto_Oct` is returning the octal representation of the input number `num`.
    If the input number is 0 or 1, it returns the integer value as a string. Otherwise, it calls the
    `convHelper` function to convert the number to octal and returns the octal representation as a
    string.
    """
    if num is None:
        print("No numeric value has been provided!")
        return
    
    octBase = ""
    if num == 0 or num == 1:
        return f"{int(num)}"
    else:
        octBase = convHelper(num)
    
    return octBase

if __name__ == "__main__":
    res = numto_Oct(43.167)
    print(f"{res}\n{type(res)}")