#!/usr/bin/env python3
import argparse
import os
import sys


def isPermNums(perm: str) -> bool:
    intput = int(perm)
    return len(perm) == 3 and intput - 777 < 1


def isPermBits(perm: str):
    if not len(perm) == 10:
        raise ValueError

    if perm[0] not in ("d", "-"):
        raise ValueError

    for i in range(1, 9, 3):
        if not (
            perm[i] in ("r", "-")
            and perm[i + 1] in ("w", "-")
            and perm[i + 2] in ("x", "-")
        ):
            raise ValueError


def main():
    parser = argparse.ArgumentParser(prog="permConv")
    parser.add_argument("perm")

    arg = parser.parse_args().perm


if __name__ == "__main__":
    sys.exit(main())
