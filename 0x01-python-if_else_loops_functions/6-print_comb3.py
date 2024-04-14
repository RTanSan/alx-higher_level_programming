#!/usr/bin/python3

for n in range(9):
    for m in range(10):
        if n != m:
            print(f"{n}{m}, ".format(n, m), end="")
