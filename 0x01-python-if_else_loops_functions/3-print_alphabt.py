#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    if (i == ord('e') or i == ord('q')):
        i += 1
    else:
        print(chr(i), end="")
        i += 1
