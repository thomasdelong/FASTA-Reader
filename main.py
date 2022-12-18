#FILE MUST BE SAVED AS FASTA.txt
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
#find key/value pair with highest gc content
GCcontentdict = {key: GCcontent(value) for (key, value) in FASTAdict.items()}
maxGCkey = max(GCcontentdict, key=GCcontentdict.get)
#print ID of sequence with highest GC content
print(f'Highest GC content:\n{maxGCkey[1:]}\n{GCcontentdict[maxGCkey]}')
