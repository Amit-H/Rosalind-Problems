def motif(dna, frag):
    '''
    Function that looks for a defined 
    DNA fragment in a DNA sequence and 
    gives the position of the start of each 
    instance of the fragment within the 
    DNA sequence.

    Input params:
    dna =  dna sequence
    frag = fragment to be searched for within 
    the sequence

    Output params:
    repeats = a list of start positions 
    of the fragment
    '''
    repeats = []
    for i in range(len(dna)):
        if frag == dna[i: i+len(frag)]:
            repeats.append(i+1)
    repeats = ''.join(str(repeats).split(','))
    return repeats

dna = "GCCGCCCTAATGAATTTAATGAATAATGAACCTACGCCTAATGAAGTAATGAAGGCTGCATAATGAACGGCTTAATGAATAATGAAGTAGTAATGAACTGTGACTAATGAAACTAATAATGAACTGTTCATAATGAATAATGAATAATGAAAGCTCTTAATGAATAATGAATAATGAATCGTGCGGCTTCTAATGAATAATGAAGAACCGTAATGAATAATGAATCACTAATGAAGACATTAATGAATATGTAATGAATAATGAATAAGTTAATGAATTTCTAATGAAGTAGTATAATGAACGCATAATGAAGTAATGAAGATCTAATGAATAATGAAATAATGAAATCCGTAATGAAACGTAATGAATAATGAACTAATTAATGAATAATGAATCGTAATGAATTTAATGAATAATGAATCCTAATGAAAAGCTAATGAATAATGAATAATGAATAATGAATAATGAAATCTAATGAAGATAATGAAGCCCACTGTAATGAACATAATGAACGCATAATGAATGTAATGAATAATGAAGTAATGAAGCATAATGAATAATGAATAATGAAATCTTAATGAAATAATGAATAATGAAGGTTAATGAATAATGAATGACGGTTAATGAAATCTAATGAAGTTTAATGAAGTAATGAACGTTGATAATGAATAATGAAGTAATGAATAATGAAGTAATGAATAATGAAACAGTAATGAATAATGAACTAATGAAATTAATGAAATTAATGAATAATGAATTTAATGAATAATGAATAATGAATAATGAATAATGAAGGCGAGGTAGAGTTTAATGAAGTTAATGAAGCTAATGAAATAATGAACTCACTAATGAA"
fragment = "TAATGAATA"

print(motif(dna, fragment))
