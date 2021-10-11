def calc_sc(c):
    length = len(c)
    values = []
    result = [0 for _ in range(1000)]
    # To construct the shingles of each document
    prev, previous_prev = 1, 0
    for i in range(2, length):
       values.append(int(f"{c[previous_prev]}{c[prev]}{c[i]}"))
       previous_prev, prev = prev, i

    # fill the 1's in the elements that are present in each document
    for i in values:
        result[i] = 1

    return result


def calc_signature(c1, c2, c3):
    # create a mapping between original index and h1/h2/h3
    n = len(c1)
    # using the hash function h1(x)=(x+1) mod 1000 generates permutations
    h1_indicies = list(range(n))
    h1_indicies.append(h1_indicies[0])
    h1_indicies = h1_indicies[1:]
    h1 = {h: o for h, o in zip(h1_indicies, range(n))}
    

    # using the hash function h2(x)=(x+2) mod 1000 generates permutations
    h2_indicies = list(range(n))
    h2_indicies.extend(h2_indicies[:2])
    h2_indicies = h2_indicies[2:]
    h2 = {h: o for h, o in zip(h2_indicies, range(n))}
    

    # using the hash function h3(x)=(x+3) mod 1000 generates permutations
    h3_indicies = list(range(n))
    h3_indicies.extend(h3_indicies[:3])
    h3_indicies = h3_indicies[3:]
    h3 = {h: o for h, o in zip(h3_indicies, range(n))}
    
    
    def signature(h):
        sig = [-1  for _ in range(3)]
        #v1,v2,v3 values stores each document row values
        for i in range(n):
            v1, v2, v3 = c1[h[i]], c2[h[i]], c3[h[i]]
            if v1 == 1 and sig[0] == -1:
                sig[0] = i
            if v2 == 1 and sig[1] == -1:
                sig[1] = i
            if v3 == 1 and sig[2] == -1:
                sig[2] = i
        return sig
    sig1 = signature(h1)
    sig2 = signature(h2)
    sig3 = signature(h3)
    print("The individual signatures of C1, C2, C3 are......")
    signatureC1 = []
    signatureC2 = []
    signatureC3 = []
    sig = [sig1, sig2, sig3]
    for i in range(len(sig1)):
        signatureC1.append(sig[i][0])
        signatureC2.append(sig[i][1])
        signatureC3.append(sig[i][2])
    print("Signature for C1",signatureC1)
    print("Signature for C2",signatureC2)
    print("Signature for C3",signatureC3)
    



def project2():
    C1= "78493157175489549376148695781578475926543918574367195748574950004752380475183459847592567467854245734860981305640100987301574865100973401839"
    C2= "93761486957815778493157175489548475926543957481857436719574953804751800047523459824573447592567467854860981305100973401856401009873015748639"
    C3= "43967243885947619758467578364710365741564736580713650134785678460164756405674567841378954623719785810765846125647561304956765996108574857876"
    sc1 = calc_sc(C1)
    sc2 = calc_sc(C2)
    sc3 = calc_sc(C3)
    calc_signature(sc1, sc2, sc3)


if __name__ == '__main__':
    project2()
