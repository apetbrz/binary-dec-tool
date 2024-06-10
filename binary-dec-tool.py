def b2d(input):
    return "d" + format(int(input[1:], 2))
def d2b(input):
    return ("" + '{0:#b}'.format(int(input[1:])))[1:]

i = 1
while i == 1:
    var = input(":")
    if(var == ""): continue
    if(var[0] == "b"):
        try: print(b2d(var))
        except: print('err')
    if(var[0] == 'd'): 
        try: print(d2b(var))
        except: print('err')
    if(var[0] == 'e'):
        exit(1)