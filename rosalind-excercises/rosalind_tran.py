from Bio import SeqIO

transition = [('A', 'G'), ('T', 'C'), ('C', 'T'), ('G', 'A')]
transversions = [('A', 'T'), ('A', 'C'), ('T', 'A'), ('T', 'G'), ('C', 'A'), ('C', 'G'), ('G', 'T'), ('G', 'C')]

dnaname, dna = [], []
with open ("rosalind_trantxt.txt",'r') as fasta:
    for seq_record  in SeqIO.parse(fasta,'fasta'):
        dnaname.append(str(seq_record.name))
        dna.append(str(seq_record.seq))

transitioncount, transversionscount = 0, 0
s1, s2 = dna

for i in range(len(s1)):
    if (s1[i], s2[i]) in transition:
        transitioncount += 1
    if (s1[i], s2[i]) in transversions:
        transversionscount += 1
print(transitioncount/transversionscount)