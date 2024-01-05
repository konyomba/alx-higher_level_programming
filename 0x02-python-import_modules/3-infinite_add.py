#!/usr/bin/python3
if __name__ == '__main__':
    import sys

allsum = 0
for i in range(len(sys.argv) - 1):
    allsum += int(sys.argv[i + i])
print("{}".format(allsum))
