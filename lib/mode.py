## Mode
# Checks if it is strippable and if rwx are in order
def main(perm: str) -> list[int]:

    # Strip first bit like the `d` in `drwxrwxrwx`
    if len(perm) == 10:
        perm = perm[1:]
    elif len(perm) == 9:
        pass
    else:
        raise ValueError

    # Checks order of ?rwxrwxrwx
    for i in range(0, 8, 3):
        if not (
            perm[i] in ("r", "-")
            and perm[i + 1] in ("w", "-")
            and perm[i + 2] in ("x", "-")
        ):
            raise ValueError


    # Raw representation in bits
    out = []

    for i in range(9):
        if perm[i] in ("r", "w", "x"):
            out.append(1)
        else:
            out.append(0)

    return out
