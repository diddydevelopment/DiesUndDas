import sys
import os

print(sys.platform)
print(sys.version)

print(sys.path)
print(sys.getrecursionlimit())


os.system("firefox "+" ".join(sys.argv[1:]))