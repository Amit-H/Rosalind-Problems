from scipy.special import comb

def mendelian_probability(k, m, n):
    '''
    Calculates the chance of getting dominant alleles in a population

    Input params:
    k = homozygous dominant
    m = heterozygous
    n = homozygous recessive
    '''
    total_population = k + m + n 
    total_combinations = comb(total_population, 2)
    dominant_combinations = comb(k, 2) + k*m + k*n + .5*m*n + .75*comb(m, 2)
    probability = dominant_combinations/total_combinations
    return probability

# Example Call: 
k = 19
m = 30
n = 29
print(mendelian_probability(k, m, n))