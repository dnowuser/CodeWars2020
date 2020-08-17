cnts = [0, 0, 0, 0, 0, 0, 0, 0]
tops = ["Pepperoni", "Red Peppers", "Pineapple", "Olives", "Sardines", "Onion", "Sausage", "Ham"]
topsVal = [32, 16, 84, 20, 12, 28, 40, 36]
types = ["Hawaiian", "Combo", "Fishaster", "Meat-Lovers", "Cheese"]
typesMap = [ #has indexes of the ingredients
[2, 7], #pineapple & ham
[1, 3, 5, 6], #red peppers & olives & onion & sausage
[4, 5], #sardines & onion
[0, 6, 7], #pepperoni & sausage & ham
[]] #no toppings
def countTops(numPiz, order):
    def multiplier(strFrac):
        if strFrac == '1/2':   return 0.5 * numPiz
        elif strFrac == '1/4': return 0.25 * numPiz
        else:                  return 1 * numPiz

    for i in range(len(order)): #Custom toppings
        for j in range(len(tops)):
            if order[i] == tops[j]:
                    cnts[j] += topsVal[j] * multiplier(order[i-1])
        for k in range(len(types)): #Types of Pizzas
            if order[i] == types[k]:
                for l in range(len(typesMap[k])):
                    cnts[typesMap[k][l]] += topsVal[typesMap[k][l]] * multiplier(order[i-1])
inputs=[]
while True:
    try: inputs.append(input())
    except EOFError: break
for i in range(len(inputs)):
    numPizAndOrder = inputs[i].split()
    numPiz, order = numPizAndOrder[0], numPizAndOrder[1:]
    countTops(int(numPiz), order)

print(f"Pepperoni: {int(cnts[0])}\n\
Red Peppers: {int(cnts[1])}\n\
Pineapple: {int(cnts[2])}\n\
Olives: {int(cnts[3])}\n\
Sardines: {int(cnts[4])}\n\
Onion: {int(cnts[5])}\n\
Sausage: {int(cnts[6])}\n\
Ham:{int(cnts[7])}")
