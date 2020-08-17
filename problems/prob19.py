def main():
    a = input()
    i = 0
    arr = []
    arr2 = []
    while True:
        num = ord(a[i])
        h1 = hex(num)
        h1 = h1[2:]
        if not h1 == '20':
            arr.append(h1)
        i += 1
        if (i == len(a)):
            break
    for i in arr:
        print (i, end = " ")
    for i in range(len(arr),0,-2):
        arr2.append(arr[i-1][1])
    print("")
    rev = arr2[::-1]
    str = ""
    for i in range(0,len(rev),1):
        str += rev[i]
    print(str)
    for i in range(0,len(str),2):
        print(chr(int(str[i:i+2],16)), end = "")
main()

