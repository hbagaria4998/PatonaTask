
"""
Complete the python function to get the output of below cases :

i) case 1: n = 1, v = 1
ii) case 2: n= 2, v = 23 (Note: 23 is derived as 1 + 22)
iii) case 3: n= 3, v = 356 (Note: 356 is derived as 1+22+333)
iv) case 4: n= 4, v = 4800 (Note: 356 is derived as 1+22+333+4444)

def mystery(n)
:

...
...
...

return v
"""



def mystery(n):
    
    v = 0
    for i in range(1,int(n)+1):
        digit = ''
        for j in range(i):
            digit = digit + str(i)
        v = v + int(digit)
    return v


print(mystery(4))