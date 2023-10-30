from Bio import SeqIO
import numpy as np
np.set_printoptions(threshold=np.inf)
def rosalind_cons():
   

   seq_name, seq_string = [], []
   with open ("rosalind_cons.txt",'r') as fasta:
      for seq_record  in SeqIO.parse(fasta,'fasta'):
        seq_name.append(str(seq_record.name))
        seq_string.append(str(seq_record.seq))

   
   str_len = len(seq_string[0])

   nucleotides = ["A", "C", "G", "T"]
   consensus_string = ""
   secondmatr = np.zeros(shape=(4, str_len), dtype=int)

   for i in range(str_len):
      p_nucleotide = [s[i] for s in seq_string]
      morefreq_nucleotide = max(p_nucleotide, key=p_nucleotide.count)
      consensus_string += morefreq_nucleotide
      for j in range(len(nucleotides)):
        secondmatr[i][j] = p_nucleotide.count(nucleotides[j])
    
   print(consensus_string)
   for i in range(len(nucleotides)):
      print("{}: {}".format(nucleotides[i], " ".join([str(j) for j in profile_matrix[i]])))

rosalind_cons()