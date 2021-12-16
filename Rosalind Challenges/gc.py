from Bio import SeqIO

def gc_counter(input_FASTA):
    '''
    This function takes a FASTA file and returns a dictionary of genes and gc content (unsorted) to the terminal

    Input params:
    input_FASTA = FASTA file

    Output params:
    dict =  dictionary using keys gene and gc_%
    '''
    dict = {
    "gene": [],
    "cg_%": []
    }
    for f in SeqIO.parse(input_FASTA, "fasta"):
        gene = f.name
        dict["gene"].append(gene)
        A = f.seq.count('A')
        C = f.seq.count('C')
        G = f.seq.count('G') 
        T = f.seq.count('T') 
        cg_percentage = float(C + G) / len(f.seq)
        dict["cg_%"].append(cg_percentage)
    
    return dict

input_FASTA = open('fasta.ffn') # replace with an actual fasta file

print(gc_counter(input_FASTA))





