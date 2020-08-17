inputs = []
degrees = 0
while True:
    try:
        inputs.append(input())
    except EOFError:
        break
for x in inputs:
    pos = x.find(":")
    hours = int(x[:pos])
    minutes = int(x[pos+1:])

    if hours >= 12:
        hours -= 12

    degmin = minutes * 6.00
    deghrs = hours*30.00 + minutes *0.50

    if abs(hours - minutes/5) > 6.00:
        if hours < 6:
            degrees = 360 - degmin + deghrs
        else:
            degrees = 360 - deghrs + degmin

    else:# hours > 0 and minutes/5 > 0:
        degrees = abs(degmin - deghrs)

    print("The angle between the Hour hand and Minute hand is " + str("{:.2f}".format(degrees)) + " degrees.")
