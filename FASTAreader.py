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
#creating an adjacency list of overlapping sequences (overlap length = k)
k=3
print("Adacency list:")
for key1, value1 in FASTAdict.items():
    for key2, value2 in FASTAdict.items():
        if value1 == value2:
            continue
        if value1[-k:] == value2[:k]:
            print(key1[1:], key2[1:])
###  GC content calculator
#find key/value pair with highest gc content
#GCcontentdict = {key: GCcontent(value) for (key, value) in FASTAdict.items()}
#maxGCkey = max(GCcontentdict, key=GCcontentdict.get)
#print ID of sequence with highest GC content
#print(f'Highest GC content:\n{maxGCkey[1:]}\n{GCcontentdict[maxGCkey]}')
###
