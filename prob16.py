ops = ["POWER", "MULTIPLY", "DIVIDE", "ADD", "SUBTRACT"]
opc = ["^", "*", "/", "+", "-"]
opf = [
lambda num1, num2: num1 ** num2,
lambda num1, num2: num1 * num2,
lambda num1, num2: num1 / num2,
lambda num1, num2: num1 + num2,
lambda num1, num2: num1 - num2
]
def mathChecker(num1, num2, op, ta):
	for i in range(5):
		if op == ops[i]:
			ans = round(opf[i](num1, num2),1)
			if ans == ta:
				print(f"{ta} is correct for {num1} {opc[i]} {num2}")
			else:
				print(f"{num1} {opc[i]} {num2} = {ans}, not {ta}")
inputs=[]
while True:
	try:
		inputs.append(input())
	except EOFError:
		break
for x in inputs:
	y = x.split()
	mathChecker(float(y[0]), float(y[1]), y[2], float(y[3]))


