import re
og, new = 'abdhmneqpywu', 'eqpywuabdhmn'
for i in range(int(input())):
	s = re.sub('[!#?,.:";\']', '', input().lower())
	table, mod = s.maketrans(og, new), "(not)"
	if s.replace(" ", "") == s[::-1].translate(table).replace(" ", ""): mod = "(is)"
	print(f"{s} {mod} {s[::-1].translate(table)}")
