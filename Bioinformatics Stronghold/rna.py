'''
This script changes DNA to RNA by changing all instances of T to U
'''

dna_string = "ACATTTCTCGGATAGGGACTTTTGTCGACGTAGGGCCCAGCGGAACCACCCAGGTCGCAGCTTCAGGACGTGCCGGCAAGTAATGATCCAAGAATACTCCACTGTGCGTTGGGAAGCGAAGACGGGTGCAAGCAGTGCTACAGCGCAGCCCCGCTTGACCTTAGGATCGCACGGTTACGTAAATACATACGACAAGATGGCGCTACGGAGGTGGGTGAGATGTTGATCGTCACAGCATCCCCCTATATTATTAATGCTTAGTACGGATTTAGTTCCCTGGGGAGCGAATCGAGCTAGAGAGAAGCTCACAGTCAAACTTCCACGACAGCGCGCCAGCCCTGCCTAGATAAACGAAGATGATATGCTGGCGTTCCGCTACCCGCGCTGTAGACGTTCAAGTTGGGATTAAGCCCGGGGACGGGATTCCTCGGCCTCGGTCTGGCTTAACAAAATTTTACAGATCCGTCATCGCATCGTTGGCTGAGTCCGAGCTTAAGTCTATGCCCCGCTTTATACATCTTTTCGGGGCCTAAGAGGGATCAACGGGAGAGCACTTGCCGAAAGGTGTCCGATAGGTACTTGCTGTTGCTTTCGTGAGTCAGGAACAGGCACCAACTCATATGGTGTTTTTACGCTCATGGGCATTTTCGCCCCGGAACACTGAAACTGATAGCCAACTTTATAACTCCCTCGGCGATGTGTGATCCAGGCGGCTTACAGGAAGAATAGGGATCCAGCTCACTCCATCCCGCGAAGGCCAGTTGCTCAAAATTGTCGAGGATAGGAGTCGAGCCCTGCGGTACCGTTTCGCAATCCTACCCGCAATCCGACTGAGTTTTTCAATCCATTCATGACTGCATCATGAGGGGGGCCCTCTCGCTACGCTGGCGAGGACGTGATACCATCGGAGGGAACATCATGATCTGACGCAGCGGCTGACTA"

def dna_to_rna(dna_string):
    '''
    Takes a DNA string and converts it to an RNA string (replacing T with U)

    Input Parameters:
    dna_string = string of DNA 

    Output Parameters:
    rna_string = string of RNA
    '''
    rna_lst = [ ]
    dna_lst = list(dna_string)
    
    for i in dna_lst:
        if i == "T":
            rna_lst.append("U")
        else:
            rna_lst.append(i)

    rna_string = ''.join(rna_lst)

    return rna_string

print(dna_to_rna(dna_string))
