keys = ["NOUNS","ADVERBS","VERBS","ADJECTIVES", ""]
nouns, adverbs, verbs, adj = [], [], [], []
groups = [nouns, adverbs, verbs, adj]
sentence = input()
words = sentence.split()
count, sec = 0, 0
while True:
    inp, go = input(), True,
    if inp == 'END': break
    if inp == keys[count]:
        sec, go = count, False
        count += 1
    go and groups[sec].append(inp)
symb = ["[N]", "[AV]", "[V]", "[AJ]"]
def replacer(words):
    for i in range(len(words)):
        for j in range(4):
            if words[i] == symb[j]:
                words[i] = groups[j][0]
                groups[j].pop(0)
    print(" ".join(words))
for i in range(2):
    replacer(words)
    words = sentence.split()
