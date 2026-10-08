## Numbers
# Checks if it's an intable str that is <778
def isNums(perm: str) -> bool:
    # Is it numbers? (777)
    try:
        intput = int(perm)
    except ValueError:
        return False
    else:
        return len(perm) == 3 and intput - 777 < 1


# Turns that '0b111' to [1, 1, 1]
def binaryList(bin: str) -> list[int]:  # Like '0b111'
    bin = bin[2:]
    out = []
    for i in bin:
        out.append(int(i))
    return out


# 777 -> [1, 1, 1, 1, 1, 1 ,1 1, 1]
def nums2Raw(perm: str) -> list[int]:
    if not isNums(perm):
        raise ValueError
    out: list[int] = []
    for i in range(3):
        out += binaryList(bin(int(perm[i])))
    return out
