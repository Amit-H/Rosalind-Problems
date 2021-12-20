from Bio import SeqIO
from collections import Counter

### Functions separated for reusability

def consensus_matrix(input_FASTA):
    '''
    Takes an input fasta file and returns a consensus
    sequence as well as the corresponding profile matrix
    
    Input params:
    input_FASTA = fasta file for parsing

    Output params:
    cons = consensus sequence
    matrix = profile sequence

    '''
    with open(input_FASTA):
        dna_strings = [str(fasta.seq) for fasta in SeqIO.parse(input_FASTA, 'fasta')]
        t = zip(*dna_strings)
        count = [Counter(column) for column in t]

        cons = ''.join([counter.most_common(1)[0][0] for counter in count])

        matrix = ''

        for base in 'ACGT':
            matrix += '{}:'.format(base)
            for counter in count:
                matrix += ' {}'.format(counter[base])
            matrix += '\n'
        matrix = matrix.rstrip()

        return cons, matrix

def consensus_matrix_joiner(cons, matrix):
    '''
    Joins consensus sequence and profile matrix

    Input params:
    cons = consensus sequence
    matrix = profile sequence

    Output params:
    joined =  cons and matrix in one output
    '''
    joined = '\n'.join([cons, matrix])
    return joined

cons, matrix = consensus_matrix(input_FASTA="fasta.txt")
print(consensus_matrix_joiner(cons, matrix))


# Help sought from this post: https://stackoverflow.com/questions/29506417/consensus-and-profile-from-rosalind-problems