#!/usr/bin/env python3
import argparse
import sys


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


## Bits
# Strip first bit like the `d` in `drwxrwxrwx`
def stripBits(perm):
    if len(perm) == 10:
        perm = perm[1:]
    elif len(perm) == 9:
        pass
    else:
        raise ValueError
    return perm


# Checks if it is strippable and if rwx are in order
def isBits(perm: str) -> bool:

    perm = stripBits(perm)

    try:
        for i in range(0, 8, 3):
            if not (
                perm[i] in ("r", "-")
                and perm[i + 1] in ("w", "-")
                and perm[i + 2] in ("x", "-")
            ):
                raise ValueError
    except ValueError:
        return False
    else:
        return True


# Turns them into raw representation in a list like [1, 1, 1, 1, 1, 1, 1, 1, 1,]
def bits2Raw(perm) -> list[int]:
    perm = stripBits(perm)
    if not isBits(perm):
        raise ValueError
    out = []

    for i in range(9):
        if perm[i] in ("r", "w", "x"):
            out.append(1)
        else:
            out.append(0)

    return out


# Arguments
def main():
    parser = argparse.ArgumentParser(prog="permConv")
    parser.add_argument("perm")

    arg = parser.parse_args().perm


if __name__ == "__main__":
    sys.exit(0)
