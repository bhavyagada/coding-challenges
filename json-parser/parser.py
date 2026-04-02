#!/usr/bin/env python3
import sys
from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("file")
    arg = parser.parse_args()

    # *** step2

    with open(arg.file, mode="r") as f: data = f.read().strip()

    if not data: sys.exit("invalid json: empty file or only whitespace")
    if data[0] != "{" or data[-1] != "}": sys.exit("invalid json: does not start with '{' and end with '}'")

    stack = []
    for ch in data:
        if ch.isspace(): continue
        elif ch == "}":
            if not stack: sys.exit("invalid json: unmatched closing bracket")
            elif (stack[-1] != '{' and stack[-1] != '"'): sys.exit("invalid json: invalid or misplaced char")
            else: stack.append(ch)
        elif ch == '"':
            if stack:
                if stack[-1] in {'{', ':', ','}: stack.append(ch)
                elif not stack[-1].isalnum(): sys.exit("invalid json: missing quote in some key")
                else: stack.append(ch)
        elif ch == ":" or ch == ",":
            if stack and stack[-1] != '"': sys.exit("invalid json: missing quote in some value")
            else: stack.append(ch)
        else: stack.append(ch)

    if stack and stack[-1] != '}': sys.exit("invalid json: unmatched opening bracket")

    print("yay! valid json!")
    sys.exit(0)

