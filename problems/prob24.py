def main(space, given, word):
    w = 11
    h = True
    board = [[0 for x in range(w)] for y in range(w)]
    blank = []
    letter = []
    for i in range(w):
        for j in range(w):
            board[i][j] = 0
    for i in range(len(space)):
        blank.append(space[i].split())
        for l in range(int(blank[i][2])):
            if blank[i][1] == "V":
                h = True
            else:
                h = False
            for j in range(int(blank[i][2])):
                if h:
                    board[int(blank[i][3])][int(blank[i][4])+l] = "_"
                else:
                    board[int(blank[i][3]) + l][int(blank[i][4])] = "_"
    for i in range(len(given)):
        letter.append(given[i].split())
        x = int(letter[i][0])
        y = int(letter[i][1])
        board[x][y] = letter[i][2]
    for i in range(len(blank)):
        for j in range(len(word)):
            if len(word[j]) == int(blank[i][2]) and blank[i][1] == "V":
                for l in range(int(blank[i][2])):
                    if board[int(blank[i][3])][int(blank[i][4]) + l] == "_":
                        continue
                    elif board[int(blank[i][3])][int(blank[i][4])+l] == "0":
                        break
                    else:
                        if word[j][l] == board[int(blank[i][3])][int(blank[i][4])+l]:
                            if int(blank[i][0]) < 10:
                                print(f"0{i+1} is {word[j]}")
                                break
                            else:
                                print(f"{i+1} is {word[j]}")
                                break

            elif len(word[j]) == int(blank[i][2]) and blank[i][1] == "H":
                for l in range(int(blank[i][2])):
                    if board[int(blank[i][3])+l][int(blank[i][4])] == "_":
                        continue
                    elif board[int(blank[i][3])+l][int(blank[i][4])] == "0":
                        break
                    else:
                        if word[j][l] == board[int(blank[i][3])+l][int(blank[i][4])]:
                             if int(blank[i][0]) < 10:
                                print(f"0{i+1} is {word[j]}")
                                break
                             else:
                                print(f"{i+1} is {word[j]}")
                                break

    #for i in range(w):
        #for j in range(w):

            #print(board[j][i], end=" ")
        #print()
    #print(blank)
    #print(letter)
    #print(word)
inputs=[]
while True:
    try:
        inputs.append(input())
    except EOFError:
        break
a = inputs.index("-------")
b = inputs.index("-------",a+1)
spacearr = []
givenarr = []
wordarr = []
for i in range(a):
    spacearr.append(inputs[i])
for i in range(a+1,b):
    givenarr.append(inputs[i])
for i in range(b+1,len(inputs)):
    wordarr.append(inputs[i])
main(spacearr,givenarr,wordarr)
