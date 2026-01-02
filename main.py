from binBase import numto_Bin
from octBase import numto_Oct
from hexBase import numto_Hex

print("""
Implemented a number conversion system for Binary (2), Octal (8), and Hexadecimal (16).

Accepts integer and fractional decimal inputs and converts them to the chosen base.
Fractional values are represented using a fixed precision of 8 fractional digits
(in the output base), with truncation.
""")

decimalBase = input("Enter a number of base 10: ")

try:
    if "." in decimalBase:
        decimalBase = float(decimalBase)
    else:
        decimalBase = int(decimalBase)
except Exception as e:
    print("\nError: Invalid Input!\nAborting!!!\n")
else:
    print("\nBases:")
    print("(2) Binary")
    print("(8) Octal")
    print("(16) Hexadecimal\n")
    
    base = input("Enter you base: ")

    match base:
        case "2":
            res = numto_Bin(decimalBase)
            print(f"\n({decimalBase})10 = ({res})2\n")
        case "8":
            res = numto_Oct(decimalBase)
            print(f"\n({decimalBase})10 = ({res})8\n")
        case "16":
            res = numto_Hex(decimalBase)
            print(f"\n({decimalBase})10 = ({res})16\n")
        case _:
            print("\nCustom base isn't allowed!\nAborting!!!\n")