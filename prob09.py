newarray = []
while True:
    x = input()
    if str(x) == "0 0":
        break
    else:
        newarray.append(x)
for elem in newarray:
    pos = elem.rfind(" ")
    minutes = int(elem[:pos])
    seconds = int(elem[(pos+1):])
    if seconds > 60:
        minutes += 1
        seconds -= 60
    if minutes == 50 and seconds > 0:
        print("Time remaining " + str(50 - minutes) + " minutes and " + str(-seconds) + " seconds (we're gonna need a bigger record)")
        break
    if seconds > 0 and minutes < 50:
        minutes += 1
    elif seconds == 0:
        seconds = 60
    if minutes > 50:
        print("Time remaining " + str(50 - minutes) + " minutes and " + str(-seconds) + " seconds (we're gonna need a bigger record)")
    elif minutes >= 25:
        print("Time remaining " + str(50 - minutes) + " minutes and " + str(60 - seconds) + " seconds (We'll need both sides)")
    else:
        print("Time remaining " + str(50 - minutes) + " minutes and " + str(60 - seconds) + " seconds")
