#!/usr/bin/python3
for m in range(0, 100):
    if m < 99:
        print(f"{m:02d}".format(), end=", ")
    else:
        print("{}".format(m))
