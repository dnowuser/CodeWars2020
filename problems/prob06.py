from collections import OrderedDict
import sys

def conv_martian(num):
    num = int(num)
    martian = OrderedDict()
    martian[1000] = "R"
    martian[900] = "BR"
    martian[500] = "G"
    martian[400] = "BG"
    martian[100] = "B"
    martian[90] = "ZB"
    martian[50] = "P"
    martian[40] = "ZP"
    martian[10] = "Z"
    martian[9] = "BK"
    martian[5] = "W"
    martian[4] = "BW"
    martian[1] = "B"

    def martian_num(num):
        for r in martian.keys():
            x, y = divmod(num, r)
            yield martian[r] * x
            num -= (r * x)
            if num <= 0:
                break


    return "".join([a for a in martian_num(num)])
inputs=[]
while True:
    try:
        inputs.append(input())
    except EOFError:
        break

for x in inputs:
    print(conv_martian(x))
