from itertools import takewhile
def main(array):
    arr1 = [None] * 2
    arr2 = [None] * 2
    arr3 = [None] * 2
    vowels = ['I','A','E','O','U']
   # vdict = {'I':lambda:print(1),'A':lambda:print(2), 'E':lambda:print(3),'O':lambda:print(4),'U':lambda:print(5) }
    a = array.split()
    num = int(a[0])
    a.pop(0)
    for i in range(0,num-1, 2):
        if i < 2:
            arr1[0] = a[i]
            arr1[1] = a[i+1]
        if arr1[0] == arr1[1]:
            print(*a, sep = ' ',end = "")
            print(" COPY")
            break
        if not arr1[0][0:2] == "SH" and arr1[1][0:3] == "SHM":
            print(*a, sep = ' ',end = "")
            print(" SHM")
            break
        if not arr1[0][0:2] == "SH" and arr1[1][0:2] == "SH":
            print(*a, sep = ' ',end = "")
            print(" RHYMING")
            break

        #print(arr1[0][max(arr1[0].rfind(i) for i in "IEAOU")])
        #print(arr1[1][max(arr1[1].rfind(i) for i in "IEAOU")])
        if vowels.index(arr1[0][max(arr1[0].rfind(i,0,len(arr1[0])-1) for i in "IEAOU")]) < vowels.index(arr1[1][max(arr1[1].rfind(i,0,len(arr1[0])-1) for i in "IEAOU")]):
           print(*a, sep = ' ',end = "")
           print(" PROGRESSIVE")
           break
        if vowels.index(arr1[0][max(arr1[0].rfind(i,0,len(arr1[0])-1) for i in "IEAOU")]) > vowels.index(arr1[1][max(arr1[1].rfind(i,0,len(arr1[0])-1) for i in "IEAOU")]):
           print(*a, sep = ' ',end = "")
           print(" ABLAUT")
           break
        if not arr1[0][0] == arr1[1][0] or arr1[0][:len(arr1[0])-4:-1] == arr1[1][:len(arr1[1])-4:-1]:
             print(*a, sep = ' ',end = "")
             print(" RHYMING")
             break
inputs=[]
while True:
	try:
		inputs.append(input())
	except EOFError:
		break
for x in inputs:
	main(x)
