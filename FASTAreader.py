#FILE MUST BE SAVED AS FASTA.txt in the same place as this program
#convert file into list of lines
def readFile(filePath):
    with open(filePath, "r") as f:
        return [l.strip() for l in f.readlines()]
#calculate percent GC content
def GCcontent(DNA):
    return round((DNA.count("C")+DNA.count("G")) / len(DNA) * 100, 4)
#convert into dictionary
FASTAfile=readFile("FASTA.txt")
FASTAdict={}
FASTAlabel=""
for line in FASTAfile:
    if ">" in line:
        FASTAlabel=line
        FASTAdict[FASTAlabel] = ""
    else:
        FASTAdict[FASTAlabel] += line

###GC content calculator
#find key/value pair with highest gc content
#GCcontentdict = {key: GCcontent(value) for (key, value) in FASTAdict.items()}
#maxGCkey = max(GCcontentdict, key=GCcontentdict.get)
#print ID of sequence with highest GC content
#print(f'Highest GC content:\n{maxGCkey[1:]}\n{GCcontentdict[maxGCkey]}')
###

###creating an adjacency list of overlapping sequences (overlap length = k)
#k=3
#print("Adacency list:")
#for key1, value1 in FASTAdict.items():
#    for key2, value2 in FASTAdict.items():
#        if value1 == value2:
#            continue
#        if value1[-k:] == value2[:k]:
#            print(key1[1:], key2[1:])
###

###generating a consensus string and a profile matrix from a list of sequences of identical length
matrix = []
for key, value in FASTAdict.items():
    matrix.append(list(value))
A=[]
C=[]
G=[]
T=[]
place=0
consensus=''
for i in range(len(matrix[0])):
    As = 0
    Cs = 0
    Gs = 0
    Ts = 0
    for list in matrix:
        base = list[place]
        if base == 'A':
            As += 1
        elif base == 'C':
            Cs += 1
        elif base == 'G':
            Gs += 1
        elif base == 'T':
            Ts += 1
    A.append(As)
    C.append(Cs)
    G.append(Gs)
    T.append(Ts)
    if A[place] > C[place] and A[place] > G[place] and A[place] > T[place]:
        consensus += 'A'
    elif C[place] > G[place] and C[place] > T[place]:
        consensus += 'C'
    elif G[place] > T[place]:
        consensus += 'G'
    else:
        consensus += 'T'
    place += 1
print(consensus)
print('A:',*A)
print('C:',*C)
print('G:',*G)
print('T:',*T)
