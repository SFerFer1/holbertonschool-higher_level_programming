#!/usr/bin/python3
p = "".join(chr(i) for i in range(97, 123)if chr(i) not in ('e', 'q'))
print("{}".format(p), end="")
