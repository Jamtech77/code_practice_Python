# Brute force
def two_sum_1(list, k):
   for i in range(len(list)):
       for j in range(1, (len(list) - i)):
           if list[i] + list[i+j] == k:
               return True
   return False

print( two_sum_1([4,7,1,-3,2], 5))
# True

list = [4,7,1,-3,2]
k = 5

# Use Two-pass Hash Table
def two_sum_2(list, k):
    ht = {}

    for i in range(len(list)):
        ht[list[i]] = i

    for i in range(len(list)):
        diff = k - list[i]
        if diff in ht:
            return True

    return False

print(two_sum_2(list, k))

'''
testcase = [] # [11, 5, 1, 6, 8, 4, 9, -2, 3, -1]

for i in range(len(list)):
    for j in range(1, (len(list) - i)):
        testcase.append(list[i] + list[i+j])

print(testcase)

for i in testcase:
    print(two_sum_1(list, i))

for i in testcase:
    print(two_sum_2(list, i))
'''
