def main(employee,rate,in1,out1,in2,out2):
    rate = float(rate[5:])
    in1 = int(in1[3:])
    if not in1 % 100 == 0:
        in1 = in1 - in1%100 + in1%100/60 * 100
    out1 = int(out1[4:])
    if not out1 % 100 == 0:
        out1 = out1 - out1%100 + out1%100/60 * 100
    in2 = int(in2[3:])
    if not in2 % 100== 0:
        in2 = in2 - in2%100 + in2%100/60* 100
    out2 = int(out2[4:])
    if not out2 % 100 == 00:
        out2 = out2 - out2%100 + out2%100/60*100
    total = ((out1-in1)/100 * rate + (out2-in2)/100 * rate)
    amount = round(total,2)
    print(employee[9:] + " earned $" + "{:.2f}".format(amount))
inputs=[]
while True:
    try:
        inputs.append(input())
    except EOFError:
        break
for x in range(0,len(inputs),6):
   main(inputs[x],inputs[x+1],inputs[x+2],inputs[x+3],inputs[x+4],inputs[x+5])


