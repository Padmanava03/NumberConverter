def my_pow(base, fractionalBits):
    ans = 1
    while fractionalBits > 0:
        if fractionalBits % 2 == 1:
            ans *= base

        base *= base
        fractionalBits //= 2

    return ans

def scale_theNum(base, num):
    if isinstance(num, float) and num != int(num):
        powBase = my_pow(base, 8)
        num = int(abs(num * powBase)) if num < 0 else int(num * powBase)
    else:
        num = int(abs(num)) if num < 0 else int(num)

    resBase = ""
    while num > 0:
        rem = num % base
        
        if base == 16:
            match rem:
                case 10:
                    rem = "A"
                case 11:
                    rem = "B"
                case 12:
                    rem = "C"
                case 13:
                    rem = "D"
                case 14:
                    rem = "E"
                case 15:
                    rem = "F"

        resBase = f"{resBase}{rem}"
        num //= base

    return resBase

def format_theOutput(resBase, num):
    c, temp = len(resBase)-1, ""
    while c >= 0:
        if isinstance(num, float) and c == 7:
            temp = f"{temp}."

        temp = f"{temp}{resBase[c]}"
        c -= 1
    
    resBase = f"0.{temp.zfill(8)}" if len(temp) <= 8 and isinstance(num, float) and num != int(num) else temp
    if num < 0:
        resBase = f"-{resBase}"

    return resBase

def convHelper(base, num):
    resBase = scale_theNum(base, num)

    resBase = format_theOutput(resBase, num)

    return resBase