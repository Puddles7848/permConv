#!/usr/bin/env python3
import argparse
import sys


# Arguments
def main():
    parser = argparse.ArgumentParser(prog="permConv")
    parser.add_argument("perm")

    arg = parser.parse_args().perm


if __name__ == "__main__":
    sys.exit(0)
