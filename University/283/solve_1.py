a=int(input())
b=int(input())
if b>=a:
    print("Wrong order!")
elif (a-b)%2==1:
    print("Wrong difference!")
else:
    base=(a-b)//2
    for i in range(base):
        print("* "*a)
    for i in range(a-base*2):
        for j in range(base):
            print("* ",end="")
        for j in range(b):
            print("  ",end="")
        for j in range(base):
            print("* ",end="")
        print()
    for i in range(base):
        print("* "*a)

# Mohammad YousefiPour