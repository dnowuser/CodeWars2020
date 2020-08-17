def main(a,b):
    a = int(a)
    b = int(b)
    if a > b:
        tmp = a
    else:
        tmp = b
    if a == 0 or b == 0:
        return 0
    else:
        while True:
            if a % tmp == 0 and b % tmp == 0:
                return tmp
            tmp -= 1

input1 = input()
input2 = input()
print(main(input1, input2))
