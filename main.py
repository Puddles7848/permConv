#!/usr/bin/env python3
import argparse
import os
import sys


def main():
    parser = argparse.ArgumentParser(prog="permConv")
    parser.add_argument("input")

    arg = parser.parse_args().input

if __name__ == "__main__":
    sys.exit(main())
