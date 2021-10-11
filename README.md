# Data-Mining-mini-project

Given the following three documents, each composed of 140 digits from {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}:
C1= 78493157175489549376148695781578475926543918574367195748574950004752380475183459847592567467854245734860981305640100987301574865100973401839
C2= 93761486957815778493157175489548475926543957481857436719574953804751800047523459824573447592567467854860981305100973401856401009873015748639
C3= 43967243885947619758467578364710365741564736580713650134785678460164756405674567841378954623719785810765846125647561304956765996108574857876
Construct the shinglesof each document, where each shingle is definedas a token of three digits(that is, k = 3). For example, the first few shinglesof C1 are 784, 849, 493, etc.Each document can thus be represented by a 1/0 vector of 1000 dimensions(10*10*10 = 1000).

1) Write a program to calculate the Jaccard similarity scores of C1, C2, C3: sim(C1, C2), sim(C2, C3), and sim(C1, C3).Your program should explicitly output thethreescores.

2) Use the following three hash functions to generate permutations and then construct the signatures of C1, C2, C3 based on the 1/0 vectors from 
h1(x): (x+1)mod 1000 
h2(x): (x+2)mod 1000
h3(x): (x+3)mod 1000 
Given the small number of permutations, use the definition of signature to implement the algorithm.Your program should output the individual signaturesof C1, C2, C3. 
