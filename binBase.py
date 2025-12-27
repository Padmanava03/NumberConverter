from helper import convHelper

def numto_Bin(num=None):
    if num is None:
        print("No number has been provided!")
        return
    
    if num == 0 or num == 1:
        return f"{int(num)}"
    else:
        binBase = convHelper(2, num)

    return binBase

if __name__ == "__main__":
    res = numto_Bin(43.167)
    print(f"{res}\n{type(res)}")