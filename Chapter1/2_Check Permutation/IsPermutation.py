# Python3

# O(N)

str_1 = "driving"
str_2 = "drivign"

def is_permutation(str_1, str_2):
	str_1 = str_1.replace(" ", "")
	str_2 = str_2.replace(" ", "")

	if len(str_1) != len(str_2):
		return False

	for c in str_1:
		if c in str_2:
			str_2 = str_2.replace(c, "")
	return len(str_2) == 0


print(is_permutation(str_1, str_2))