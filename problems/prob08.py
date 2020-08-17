def main(text):
    index = 0
    i = 0
    while len(text) - i > 80:
        if len(text) - i < 80:
            break
        else:
            index = text.rfind(" ",i,i+81)
        if index == -1:
            break
        tmp = text[0:index] + "\n" + text[index + 1:]
        text = tmp
        i = index + 1
    print(text)
inputs=[]
while True:
    try:
        inputs.append(input())
    except EOFError:
        break
for x in inputs:
   main(x)

