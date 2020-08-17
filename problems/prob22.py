stringA = ["A", "B", "B", "C", "D", "D", "E", "E", "F", "G", "G", "A", "A", "A"]
stringE = ["E", "F", "G", "G", "A", "A", "B", "B", "C", "D", "D", "E", "E", "E"]
stringAr= ["A", " ", "B", "C", " ", "D", " ", "E", "F", " ", "G", " ", "A"]
stringEr= ["E", "F", " ", "G", " ", "A", " ", "B", "C", " ", "D", " ", "E"]
strings = [stringAr, stringEr]
def guitar(inp):
	if len(inp)>1:
		fret, string = int(inp.split()[0]), inp[-1]
		if string == "E": print(stringE[fret+1])
		else:      		  print(stringA[fret+1])
	else:
		note = inp[0]
		def findNotes(w):
			build = ''
			for i in range(len(strings[w])):
				if note == strings[w][i]:
					build += f"{i} {strings[w][0]} "
			return build
		print(findNotes(1) + findNotes(0))
inputs=[]
while True:
    try: inputs.append(input())
    except EOFError: break
for i in range(len(inputs)):
	guitar(inputs[i])

