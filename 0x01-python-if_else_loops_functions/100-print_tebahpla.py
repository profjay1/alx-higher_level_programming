#!/usr/bin/python3
signal = 0
for i in range(ord('z'), ord('a') - 1, -1):
    print(chr(i - signal), end="")
    if signal == 0:
        signal = 32
    else:
        signal = 0
