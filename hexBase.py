from helper import convHelper

def numto_Hex(num=None):
    if num is None:
        print("No numeric value has been provided!")
        return
    
    if num == 0:
        return f"{int(num)}"
    else:
        hexBase = convHelper(16, num)
    
    return hexBase

if __name__ == "__main__":
    res = numto_Hex(43.167)
    print(f"{res}\n{type(res)}")