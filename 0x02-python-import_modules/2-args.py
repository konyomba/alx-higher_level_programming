#!/usr/bin/python3
if __name__ == '__main__':
    import sys

sys.argv
if sys.argv == 0:
    print(":", end="\n")
elif sys.argv == 1:
    print(len(sys.argv), "arguement :")
else:
    print(len(sys.argv), "arguement:", end="\n")
    for i in range(0, len(sys.argv)):
        print(i, sys.argv)
