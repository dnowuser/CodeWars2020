def main(inputs):
	yen, numItems = splitAssign(0)
	itemMap = {}
	for i in range(1, numItems+1):
		itemMap[splitAssign(i,0)] = splitAssign(i,1)
	orderedItems = sorted(itemMap, key=lambda item: item[1])

	cantCnt = 0

	for item in orderedItems:
		if yen - itemMap[item] >= 0:
			print(f"I can afford {item}")
			yen -= itemMap[item]
		else:
			print(f"I can't afford {item}")
			cantCnt += 1
	if cantCnt == numItems:
		print("I need more Yen!")
	print(yen)

def splitAssign(inputNum, which=2):
	splitList = str(inputs[inputNum]).split()
	if which == 0:
		return str(splitList[0])
	elif which ==1:
		return int(splitList[1])
	else:
		return int(splitList[0]), int(splitList[1])

inputs=[]
while True:
    try:
        inputs.append(input())
    except EOFError:
        break

main(inputs)
