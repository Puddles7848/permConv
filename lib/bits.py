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
