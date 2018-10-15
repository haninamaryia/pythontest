
def is_valid_float(string):
    try:
        float(string)
    except ValueError:
        return False
    else:
        return True
s1=''
s2=''
while (True):
    s1=input('input first string: ')
    s2=input('input second string: ')
    if (is_valid_float(s1) and is_valid_float(s2)):
        break

s1=float(s1)
s2=float(s2)

if s1>s2:
    print(str(s1)+" is greater than "+str(s2))
elif s1==s2:
    print(str(s2)+" is equal to "+str(s1))

else:
    print(str(s2)+" is greater than "+str(s1))


