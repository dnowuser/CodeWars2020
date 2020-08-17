#yard = 91.44 cm
#foot = 30.48 cm
#inch = 2.54 cm
def main(measure):
    x = measure.split()
    if len(x) == 3:
        yd = int(x[0])
        ft = int(x[1])
        inch = int(x[2])
    if len(x) == 2:
        yd = int(x[0])
        ft = int(x[1])
        inch = 0
    if len(x) == 1:
        yd = int(x[0])
        ft = 0
        inch = 0
    cm = yd * 91.44 + ft * 30.48 + inch * 2.54

    print("{:0.2f}".format(cm))




inputs=[]
while True:
    try:
        inputs.append(input())
    except EOFError:
        break

for x in inputs:
   main(x)
