# Python3

# O(N)

'''
Problem Stmt: Is Unique: Implement an algorithm to determine if a string has all unique characters.

What if you can't use additional data structures ?

Hints: 

#44, #117, #132

#44 - you can try a hash table

#117 - bit vector be useful

#132 - can you solve it in O(N logN)

Approach:

[ F F F F F F F ] --> we can create an array of bool values, initally False maybe.

We can return false if the string len exceeds the num of unique char in alphabets.

for example:

	mother = Strlen(6)
             uniqueChar(6)

    uniqueChar == Strlen, So return true

    mood = Strlen(4)
           uniqueChar(3)

    uniqueChar != Strlen, So return false
'''

# Solution:

import unittest

def isUnique(str):
	# delete whitespaces
	str = str.replace(' ', '')
	# convert to similar cases
	str = str.lower()
	# check length of str
	if len(str) > 256:
		return False

	else:
		for i in range(len(str)):
			for j in range(i+1, len(str)):
				if str[i] == str[j]:
					return False
		return True

# print(isUnique('mood'))
# print(isUnique('mother'))

class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = isUnique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = isUnique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()


