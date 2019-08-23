# relation generator
#adapted from DeWitt: Wisconson Benchmark, Second Draft
#IG
#
import sys #args

SA = "'AAAA" + 45*'x' + "'"
#generates strings based on int input
def convert(unique):
    result = list('AAAAAAA')
    rem = i = 6
    su4 = unique % 4
    r = "'AAAAAAA" + 45*'x' + "'"

    while unique > 0:
        rem = unique % 26
        result[i] = chr(ord('A') + rem) #increment char by remainder
        unique = unique // 26
        i -= 1
        rtemp = ''.join(result) + 45*'x' #collapse to string and append x's
        r = "'" + rtemp + "'"

    if su4 > 2:
        s4 = "'VVVV" + 45*'x' + "'"
    elif su4 > 1:
        s4 = "'OOOO" + 45*'x' + "'"
    elif su4 > 0:
        s4 = "'HHHH" + 45*'x' + "'"
    else:
        s4 = "'AAAA" + 45*'x' + "'"

    return (r,s4)

def randGen(s, l, g, p):
    f = True
    while f:
        s =  g * s % p #seed * generator mod prime
        if s < l: #seed within limit
            f = False
    return s

def generate_relation(tups, gen, prim, head=False):
    seed = gen
    u1 = u2 = two = four = twenty = 0
    oneP = tenP = twentyP = fiftyP = 0
    u3 = evenOneP = oddOneP = 0
    s1 = s2 = s4 = ""
    if head:
        print("u1,u2,two,four,ten,twenty,oneP,tenP,twentyP,fiftyP,u3,evenOneP,oddOneP, s1, s2, s4")
    for i in range(0,tups):
        seed = randGen(seed, tups, gen, prim)
        u1 = seed - 1
        u2 = i
        two = i % 2
        four = i % 4
        ten = i % 10
        twenty = i % 20
        oneP = i % 100
        tenP = ten
        twentyP = i % 5
        fiftyP = two
        u3 = u1
        evenOneP = oneP * 2
        oddOneP = oneP *2 + 1
        s1,_ = convert(u1)
        s2,s4 = convert(i)
        print(u1,u2,two,four,ten,twenty,oneP,tenP,twentyP,fiftyP,u3,evenOneP,oddOneP, s1, s2, s4,sep=',')#, end='')


def main():
    tupCount = int(sys.argv[1]) if len(sys.argv) > 1 else 10 #first arg sets tuple count, default 10
    headers = True if len(sys.argv) > 2 else False #enable header printing with any second arg
    
    if tupCount <= 1000:
        generator = 279
        prime = 1009
    elif tupCount <= 10000: 
        generator = 2969
        prime = 10007  
    elif tupCount <= 100000:
        generator = 21395
        prime = 100003
    elif tupCount <= 1000000:
        generator = 2107
        prime = 1000003 
    elif tupCount <= 10000000:
        generator = 211
        prime = 10000019   
    elif tupCount <= 100000000:
        generator = 21
        prime = 100000007 
    else: 
        print("too many rows requested\n")
        exit(0)

    generate_relation(tupCount, generator, prime, headers)
 

####fin
if __name__ == '__main__':
    main()


