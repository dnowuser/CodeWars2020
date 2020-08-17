def main(a,b):
    a = int(a)
    b = int(b)
    if a > b:
        greater = a
    else:
        greater = b
    if a == 0 or b == 0:
        return 0
    else:
        while True:
            if greater % a == 0 and greater % b == 0:
                return greater
            greater += 1

input1 = input()
input2 = input()
print(main(input1, input2))
