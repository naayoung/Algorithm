import sys
input = sys.stdin.readline

name = input().strip()

if name == "M":
    print("MatKor")
elif name == "W":
    print("WiCys")
elif name == "C":
    print("CyKor")
elif name == "A":
    print("AlKor")
else:
    print("$clear")