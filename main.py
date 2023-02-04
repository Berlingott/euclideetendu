def euclideEtendu(a, b,call):
    # Base Case
    if a == 0:
        print(call,"fin", "a:",a,"b:",b)
        return b, 0, 1
    else:
        print(call,"appel avant mod:","a:",a,"b:",b)
        gcd, x, y = euclideEtendu(b % a, a,call+1)
        print(call,":","a:",a,"b:",b,"t:",gcd,"x:",x,"y:",y)
        return gcd, y - (b // a) * x, x


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nombredeprint = 1
    e = 17
    p = 53
    q = 73
    n = p * q
    phi = (p - 1) * (q - 1)
    m=3

    print (nombredeprint, e, p, q, n, phi)
   # euclide(e, On)
    y,x,d = euclideEtendu(phi,e,0)
    print d,x,y

    print ("preuve:",e*d%phi)
    print "clef chiffrement"
    print (m**e)
    print n
    c = (m**e)%n
    print c

    print "clef dechiffrement"
    print ((c**d)%n)%n

    print(681**881)
#Il suffit donc de prendre d=x.



# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# d sense etre 881