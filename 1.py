def calc_sc(c):
    length = len(c)
    values = []
    result = [0 for _ in range(1000)]
    prev, previous_prev = 1, 0
    # To construct the shingles of each document
    for i in range(2, length):
       values.append(int(f"{c[previous_prev]}{c[prev]}{c[i]}"))
       previous_prev, prev = prev, i

    # fill the 1's in the elements in a set
    for i in values:
        result[i] = 1

    return result


def sim(c1, c2):
    union = 0
    intersection = 0
    for x, y in zip(c1, c2):
        union += 1 if x+y > 0 else 0
        intersection += 1 if x == y == 1 else 0
    return intersection / union


def project1():
    C1= "78493157175489549376148695781578475926543918574367195748574950004752380475183459847592567467854245734860981305640100987301574865100973401839"
    C2= "93761486957815778493157175489548475926543957481857436719574953804751800047523459824573447592567467854860981305100973401856401009873015748639"
    C3= "43967243885947619758467578364710365741564736580713650134785678460164756405674567841378954623719785810765846125647561304956765996108574857876"
    sc1 = calc_sc(C1)
    sc2 = calc_sc(C2)
    sc3 = calc_sc(C3)
    jaccard_sim12 = sim(sc1, sc2)
    jaccard_sim23 = sim(sc2,sc3)
    jaccard_sim31 = sim(sc3, sc1)
    print(f"Sim(C1, C2) = {jaccard_sim12}")
    print(f"Sim(C2, C3) = {jaccard_sim23}")
    print(f"Sim(C3, C1) = {jaccard_sim31}")

if __name__ == '__main__':
    project1()
