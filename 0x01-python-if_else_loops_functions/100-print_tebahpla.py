#!/usr/bin/python3
for i in reversed(range(0, 26)):
    if i % 2 == 0:
        num = i + 65
    else:
        num = i + 97
    print("{}".format(chr(num)), end="")
