def main(num):
    center = False
    count = 0
    num = int(num)
    b = bin(num).replace("0b","")
    a = str(b)
    if len(a) % 2 == 0:
        print (f"{num} no")
        return 0
    elif a[int(len(a)/2)] == '0':
        center = True
    for i in range(len(a)):
        if a[i] == '0':
            count += 1
    if center and count == 1:
        print(f"{num} yes")
        return 0
    else:
        print(f"{num} no")
        return 0


inputs=[]
while True:
    try:
        inputs.append(input())
    except EOFError:
        break

for x in inputs:
   main(x)
