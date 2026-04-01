#!/usr/bin/env python3
import sys
from argparse import ArgumentParser

def get_counts(file: str) -> tuple[int]:
    byte_count = char_count = word_count = line_count = 0
    with open(file, mode="rb") as f:
        for line in f:
            byte_count += len(line)
            char_count += len(line.decode())
            word_count += len(line.split())
            line_count += 1
        return byte_count, char_count, word_count, line_count

if __name__ == "__main__":
    parser = ArgumentParser(prog="wc.py", usage="%(prog)s [-clmw] [file ...]")
    parser.add_argument("-c", action="store_true", default=False, help="The number of bytes in each input file is written to the standard output.")
    parser.add_argument("-l", action="store_true", default=False, help="The number of lines in each input file is written to the standard output.")
    parser.add_argument("-w", action="store_true", default=False, help="The number of words in each input file is written to the standard output.")
    parser.add_argument("-m", action="store_true", default=False, help="The number of characters in each input file is written to the standard output.")
    parser.add_argument("file", nargs="*")
    args = parser.parse_args()

    for file in args.file:
        bytes_, chars_, words_, lines_ = get_counts(file)
        out = []
        if args.l: out.append(lines_)
        if args.w: out.append(words_)
        if args.c: out.append(bytes_)
        if args.m: out.append(chars_)
        if not any([args.c, args.l, args.w, args.m]): out.extend([lines_, words_, bytes_])
        print(f"{" ".join(map(str, out))} {file}")

    if not args.file:
        data = sys.stdin.buffer.read()
        bytes_ = len(data)
        lines_ = data.count(b'\n')
        text = data.decode()
        chars_ = len(text)
        words_ = len(text.split())
        out = []
        if args.l: out.append(lines_)
        if args.w: out.append(words_)
        if args.c: out.append(bytes_)
        if args.m: out.append(chars_)
        if not any([args.c, args.l, args.w, args.m]): out.extend([lines_, words_, bytes_])
        print(f"{" ".join(map(str, out))}")

