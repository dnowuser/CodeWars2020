def main(x):
    x = str(x)
    if x[0] == '-':
        return int('-' + x[-1:0:1])
    else:
        return int(x[::-1])

inputText = input()
print(main(inputText))


