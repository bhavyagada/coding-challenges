#!/usr/bin/env python3
import sys
from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("file")
    arg = parser.parse_args()

    # *** step1

    with open(arg.file, mode="r") as f: data = f.read().strip()

    if not data: sys.exit("invalid json: empty file or only whitespace")
    if data[0] != "{" or data[-1] != "}": sys.exit("invalid json: does not start with '{' and end with '}'")

    stack = []
    for ch in data:
        if ch == "}":
            if not stack: sys.exit("invalid json: unmatched closing bracket")
            stack.pop()
        else: stack.append(ch)
    if stack: sys.exit("invalid json: unmatched opening bracket")

    print("yay! valid json!")
    sys.exit(0)

