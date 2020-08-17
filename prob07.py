def main(color):
    split = color.find(' ')
    a = color[:split]
    b = color[split + 1:]

    #colors = ["red","blue","yellow","Purple","Orange","Green","White","Black"]
    if not b == "WHITE" and not b == "BLACK":
        if a == "WHITE":
            print(f"LIGHT {b}")
            return 0
        if a == "BLACK":
            print(f"DARK {b}")
            return 0
    if not a == "WHITE" and not a == "BLACK":
        if b == "WHITE":
            print(f"LIGHT {a}")
            return 0
        if b == "BLACK":
            print(f"DARK {a}")
            return 0
    if a == "RED" and b == "BLUE" or a == "BLUE" and b == "RED":
        print("PURPLE")
        return 0
    if a == "RED" and b == "YELLOW" or a == "YELLOW" and b == "RED":
        print("ORANGE")
        return 0
    if a == "BLUE" and b == "YELLOW" or a == "YELLOW" and b == "BLUE":
        print("GREEN")
        return 0
    if a == b:
        print(f"{a}")
        return 0

inputs=[]
while True:
    try:
        inputs.append(input())
    except EOFError:
        break

for x in inputs:
    main(x)
