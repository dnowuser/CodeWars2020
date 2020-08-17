def main(series):
    numbers = list(map(int, series.split()))
    length = len(numbers)
    value = 0
    vdict = {1: "X^3", 2: "X^2", 3: "Geometric", 4: "Geometric (With Gaps)", 5: "Fibonacci"}
    for i in range(length-1):
        if (numbers[i+1] % numbers[i] ** 3 == 0):
            value = 1
        else:
            value = 0
            break
    if value == 0:
        for i in range(length-1):
            if numbers[i + 1] % numbers[i] ** 2 == 0:
                value = 2
            else:
                value = 0
                break
    if value == 0:
        for i in range(length-2):
            if numbers[i + 2] / numbers[i + 1] == numbers[i + 1] / numbers[i]:
                value = 3
            else:
                value = 0
                break
    if value == 0:
        for i in range(length-2):
            if numbers[i] / numbers[i + 1] == numbers[i + 1] / numbers[i + 2]:
                value = 3
            else:
                value = 0
                break
    if value == 0:
        for i in range(length-2):
            if (numbers[length-1] / numbers[i]) % (numbers[i + 1] / numbers[i]) == 0:
                value = 4
            else:
                value = 0
                break
    if value == 0:
        for i in range(length-2):
            if (numbers[i] / numbers[length-1]) % (numbers[i] / numbers[i+1]) == 0:
                value = 4
            else:
                value = 0
                break
    if value == 0:
        for i in range(length-2):
            if((numbers[i+2] - numbers[i+1]) == numbers[i]):
                value = 5
            else:
                value = 0
                break
    #print(*numbers, end = " ")
    if value == 0:
        print(*numbers, end = "")
        print(" is an Unknown Series")
    else:
        print(vdict[value])


inputs=[]
while True:
	try:
		inputs.append(input())
	except EOFError:
		break
for x in inputs:
	main(x)
