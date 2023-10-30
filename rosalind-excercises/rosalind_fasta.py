from Bio import SeqIO
def rosalind_gc1(dna):
    numgc = dna.count('G') + dna.count('C')
    totalnuc = len(dna)
    pergc = (numgc / totalnuc) * 100
    return pergc

def rosalind_gc2(fasta):
    highest_gc = 0
    highest_gc_id = ""

    for record in SeqIO.parse(fasta, "fasta"):
        pergc = rosalind_gc1(record.seq)
        if pergc > highest_gc:
            result = pergc
            resultid= record.id

    return resultid, result



highest_gc_id, highest_gc = rosalind_gc1('rosalind_gc.txt')

print(highest_gc_id)
print("{:.6f}".format(highest_gc))