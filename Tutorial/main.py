from math import *
import random

s = "Hello, World!"
num = 52

print(s.replace("He", "Hi"))

print(pi)

# n1 = input("num1: ")
# n2 = input("num2: ")
# r = float(n1) + float(n2)
# print(r)

friends = ["K", "P", "J", "A", "O", "W"]
nums = [2, 4, 6, 12, 23, 45]
friends.insert(2, "HELLO")
friends.remove("O")
# friends.extend(nums) # 往後延長
friends.pop()  # remove the last one
friends.sort()
nums.reverse()
f2 = friends.copy()
# print(f2)
# print(friends)


# Tuples  can't be modified
zahyou = (4, 5)
print(zahyou[0])


# function
def say_hi():
    print("Hi")


def call_name(name):
    print("Hi, " + name)


say_hi()
call_name("James")


def cube(num):
    return num * num * num


result = cube(5)
print(result)

is_male = False
is_tall = True

if is_male and is_tall:
    print("male or tall or both")
elif is_male and not (is_tall):
    print("short male")
elif not (is_male) and is_tall:
    print("not male but tall")
else:
    print("neither male nor tall")


def max_num(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    elif n3 >= n1 and n3 >= n2:
        return n3


re = max_num(5, 80, 9)
print(re)


l = "d"
if l in "abcdfefg":
    print("Yes, it's inside")

a = 3
if a in [1,2,3,4,5,6,7,8,9,10]:
    print("a is included")


"""""
n1 = float(input("1st number: "))
op = input("Enter operaotr:" )
n2 = float(input("2nd number"))

if op == "+":
    print(n1 + n2)
elif op == "-":
    print(n1 - n2)
elif op == "*":
    print(n1 * n2)
elif op == "/":
    print(n1 / n2)
else:
    print("Invalid operator")
"""""

#Dictionary
monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    1: 10,
    2: 60,
    10: 123

}

print(monthConversion[2])
print(monthConversion.get("Apr", "Not found"))

i = 0
while i <= 10:
    print(i)
    i += 1

"""""
msg = ""
while msg != "Bye":
    msg = input(">>")
    print("拍拍")
"""

for letter in "Hello World!":
    print(letter)

for index in range(10): #0~9
    print(index)

#range(L,U,step)可設間隔
for i in range(1,15,2):
    print(i)


Friends = ["Jim", "Karen", "Kevin", "John"]

for name in Friends:
    print(name)

for index in range(len(Friends)):
    print(Friends[index])


for i in range(10):
    print(i)


def asd_re(a1, a2):
    asd = [3, 5]
    if a1 == 1:
        return 1
    return asd

x = asd_re(0,2)
print(x)



for x in range(0,10):
  print(x)
  random.randint(0,9)



n = random.sample(range(0,10), 4)
rand_str = ""
for index in range(0, 4):
    rand_str += str(n[index])

print(n)
print(rand_str)


#取亂數0~9
temp = 0
k = 0
rand_list = [0,1,2,3,4,5,6,7,8,9]

for i in range(0, 10):
    k = random.randint(i, 9)
    temp = rand_list[k]
    rand_list[k] = rand_list[i]
    rand_list[i] = temp

print(rand_list)


#Exponent Function
def raise_to_power(base_num, pow_num):
    result = 1
    for i in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(5,3))




num_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(num_grid[0][0])

for row in num_grid:
    for column in row:
        print(column)




def translate(phrase):
    trans = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":  #vowel
            if letter.isupper():
                trans = trans + "G"
            else:
                trans = trans + "g"
        else:
            trans = trans + letter
    return trans

print(translate("ninoadAAddOoo"))


#Except   可避免適用者的錯誤輸入
try:
    a = 10 / 0
    #number = int(input(">>"))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid input")
except: #if something error
    print("Invalid Input")



name_file = open("name_list.txt", "r")  #"r"/"w"/"a"/"r+"
                                        #"a" means append
                                        #"w" overwrite
print(name_file.readable())

#print(name_file.read())    #read all

#print(name_file.readline())

#print(name_file.readlines())

#print(name_file.readlines()[1])

for i in name_file.readlines():
    print(i)


name_file.close()


#增加內容到檔案中
append_file = open("create_file.txt", "a")

append_file.write("\nHello world!!!!!!\nHello world!!!!!!")

append_file.close()

append_file = open("create_file.txt", "r")
print(append_file.read())
append_file.close()


#複寫檔案 將原有的檔案清除血新的進去
append_file = open("create_file.txt", "w")

append_file.write("overwrite the text")

append_file.close()

append_file = open("create_file.txt", "r")
print(append_file.read())
append_file.close()




#module 自訂
import useful_tools

print(useful_tools.roll_dice(10))


#定義Classes和物件(object)
     #from file     #import class
from student import Student

student1 = Student("Jim", "Business", 2.1, False)
student2 = Student("Jane", "Art", 3.8, True)
print(student1.name)
print(student2.gpa)

#Put function inside the class
print(student2.on_honor_roll())



#Building a Multiple Choice Quiz
from Question import Question

question_prompts = [
    "Which one is correct? \n(a)Pikachu\n(b)Winnie\n(c)Coffee\n",
    "What color are bananas? \n(a)Blue\n(b)Yellow\n(c)Red\n",
    "Where do you live? \n(a)Taichung\n(b)Taipei\n(c)Changhua\n"
]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a"),
]

def run_test(questions):
    score = 0
    for Q in questions:
        ans = input(Q.prompt)
        if ans == Q.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct!")

#run_test(questions)



#Inherit(繼承)
from chef import Chef
from ChineseChef import ChineseChef

myChef = Chef()
myChef.make_salad()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_fried_rice()
myChineseChef.make_special_dish()

