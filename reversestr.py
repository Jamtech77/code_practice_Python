Input = 'ABCDEF'

def Reverse_Str(s):
    list_str = list(s)
    l = len(s)
    out = ''
    for i in range(l):
        out += ''.join(list_str[l-1-i])
    return out

def Reverse_easy(x):
  return x[::-1]


print(Input)
s = Reverse_Str(Input)
print(s)

s1 = Reverse_easy(Input)
print(s1)