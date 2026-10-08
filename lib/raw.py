## Raw
# Binary to decimal
def bin2Dec(number: str) -> str:
    return str(int(number, 2))


# Raw to bits
def raw2Bits(bits: list) -> str:
    if len(bits) != 9:
        raise ValueError
    out: str = "?"
    for i in range(9):
        if bits[i]:
            if i%3 == 0:
                out += "r"
            elif i%3 == 1:
                out += "w"
            elif i%3 == 2:
                out += "x"
            else:
                raise ValueError
        else:
            out += "-"

    return out


# Raw to nums
def raw2Nums(nums: str) -> str:
    if len(nums) != 9:
        raise ValueError
    out: str = ""
    for i in range(3):
        tmp: str = ""
        for j in range(3):
            tmp += str(nums[i*3+j])
        out += bin2Dec(tmp)
    return out
