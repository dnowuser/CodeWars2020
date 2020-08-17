def main (a,b):
    if a == '0' and b == '0':
        return 0
    else:
        print(f"{inputs[counter]}\n" + inputs[counter+1])
        line1 = inputs[counter].split()
        for i in range(len(line1)):
            line1[i] = line1[i].lower()
        line2 = inputs[counter+1].split()
        for j in range(len(line2)):
            line2[j] = line2[j].lower()

        common = set(line1).intersection(set(line2))
        print(len(common), end=" ")
        for word in common:
            print(word, end = " ")
        print("")
inputs=[]
while True:
    try:
        inputs.append(input())
    except EOFError:
        break
counter = 1
for x in inputs[::3]:
    a = x.split()
    main(a[0],a[1])
    counter += 3
