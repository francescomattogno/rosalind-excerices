from Bio import SeqIO 
def parse_fasta():                     
   sequences = []                             
   handle = open('lcsm.txt', 'r')     
   for record in SeqIO.parse(handle, 'fasta'):
    sequences = []                          
    seq = ''                               
    for nt in record.seq:                  
        seq += nt                          
    sequences.append(seq)                  
   handle.close()
   return sequences      

def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and all(data[0][i:i+j] in x for x in data):
                    substr = data[0][i:i+j]
    return substr

def is_substr(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True
print(long_substr(parse_fasta()))