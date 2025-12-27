from helper import convHelper

def numto_Oct(num=None):
    if num is None:
        print("No numeric value has been provided!")
        return
    
    octBase = ""
    if num == 0 or num == 1:
        return f"{int(num)}"
    else:
        octBase = convHelper(8, num)
    
    return octBase

if __name__ == "__main__":
    res = numto_Oct(-8.0)
    print(f"{res}\n{type(res)}")