def rosalind_rna():
    dna='GGCGCCTTTATAAGCGAATAAAGTCCGGGTTTCCCGGCGACGTGAAACATGACCACGCTTAGTTAAGGCTGGCCCAGGTCGGCGCCGCTAGCAACTCCTTTATAAGTAGTTCCCAAAACGTAGGGTTGACGACGACGGCCACCGTGGCCTCGTCCTATCTCGGGTCCATGCCTCACTGCGACCGACCGTGCAGGCCTTATGGCTTCACAAAACCTACCGCTACCGGATCGTGTCTTCTACGCGCGCTTTACGACGACGTTATCTGCACGGCTTTCAACGAAGTACTCGATGAGCGAGACCAGTCACGCCACCTTCTCGCCTTGCAGCGGCCCCGAAGCTAAGTTATTAGAATGAAGGATCTGAACAATTATGCAGACCAGATGTCTGGACTGTGTTAGCTTCCCGAATGCGGATTTCCTACCGCAAATCCGGCTGTACTATCGGTCTCGCAAAGCCGGCCTACACAGGGGTTTATCCCCCGACTGGATCGATTCATACATGGCATGTGGTAACGAACAGTTGCTGTGCTGGGGGCACTTCGGTACACTTCCCACGTGCTCTTCGCAACTCCATATTCGCTGATTGCTTATCTCTGGATCGAAACTTATTGGGGTACCATTACAGAAGGGTCCTCATGCAGCACAGATTGGAACGTCAGACGTTGTCATAGTCATTATGGAAGTCGAGCGGAAACCTGCGACCGACAAGTAATACGTCTGGGGAACTTAAACCGGCCAAGTGTTGATTACTAGCGATAGACCAAAAGCTCCACCACATGCCTGCAGCTATCGATGTACAGGGTCCTCTATGATCTAGATTAGTCGGTATTTGAGATCGTGTAAGCGCTCCCTGCATGTGAACTGCCATCTGTAAGCGCTCATGTGGCCGATACTAAATAGCTCGCCGGGTTTGTATGTCGGGCACTAGATGAGTCCCATTACACTCTCATGAAGGTGGGGTGCAAAGGAGCTGGTTCGATTTTCCAAATTAACCT'
    rna=dna.replace('T', 'U')
    print(rna)
    
rosalind_rna()