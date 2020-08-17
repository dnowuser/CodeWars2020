def main(a):
    a = int(a)
    if (a <= 1) :
        print (f"{a} is NOT Prime")
        return
    if (a <= 3) :
        print(f"{a} is PRIME")
        return
    if (a % 2 == 0 or a % 3 == 0) :
        print (f"{a} is NOT Prime")
        return
    i = 5
    while(i * i <= a) :
        if (a % i == 0 or a % (i + 2) == 0) :
             print (f"{a} is NOT Prime")
             return
        i = i + 6
    print(f"{a} is PRIME")
    return

input1 = input()
main(input1)

