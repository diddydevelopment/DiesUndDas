a = 6

for e in range(a-1):
    for z in range(a-e-2):
        print(" ",end="")
    for z in range(e*2+1):
        print("#",end="")
    print()
for e in range(a-2):
    print(" ",end="")
print("#")


l = list(range(a-1))+[0];
for e in l:
  print(" "*(a-2-e),end="")
  print("#"*(e*2+1))

[print(" "*(a-2-e)+"#"*(e*2+1)) for e in list(range(a-1))+[0]]