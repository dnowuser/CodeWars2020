def main(a, b):
    oddcount = 0
    evencount = 0
    aint = int(a)
    bint = int(b)
    j = a
    numcount = 0
    for i in range(aint,bint):
        oddcount = 0
        evencount = 0
        for x in range(0,len(j)):
            tmp = len(b) - x - 1
            if tmp % 2 == 1:
                oddcount += int(j[x])
            else:
                evencount += int(j[x])
        if oddcount == evencount:
            print(f"{j} ", end="")
            numcount += 1

        i += 1
        j = str(i)
    if numcount == 0:
        print("No Numbers found with Equal Sum in the given range!!")
in1 = input()
in2 = input()
main(in1,in2)
