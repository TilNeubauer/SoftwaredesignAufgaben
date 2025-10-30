
def roman2arabic(roman: str) -> int:
    r2a = {
    "I": 1, "V": 5, "X": 10,
    "L": 50, "C": 100, "D": 500,
    "M": 1000
    }

    str2int = []
    for c in roman: 
        str2int.append(r2a[c])

    arabic = 0
    for i, num in enumerate(str2int):
        if i < len(str2int)-1:
            if num >= str2int[i+1]:
                arabic += num
            else:
                arabic -= num
        else: 
            arabic += num

    return arabic

def main() -> None:

    print(roman2arabic("MMMDCCXXIV"))
    print(roman2arabic("MXCIV"))
    print(roman2arabic("VIII"))

if __name__ == "__main__":
    main()