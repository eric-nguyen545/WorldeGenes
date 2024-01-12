def durdle_match(guess, target):
    '''
    Purpose: Take in two strings and return a string that tells the player if the letters are correct
    Parameters:
        guess: a player's guess
        target: the word the player is attempting to guess
    Return Value: a string consisting of G, Y, or B.
            G: This letter in the guess appears in the same location in the target string
            Y: This letter in the guess appears in the target string in another location
            B: This letter in the guess does not appear in the target string
    '''
    output = ''
    for x in range(len(guess)):
        if guess[x] == target[x]:
            output += 'G'
        elif guess[x] in target:
            output += 'Y'
        else:
            output += 'B'
    return output
        
def durdle_game(target):
    '''
    Purpose: A function that takes in a word and lets the user try and guess it
    Parameters:
        target: the word the user is trying to guess
    Return Value: The number of guesses it took the user to guess the word

    '''
    x = len(target)
    print(f'Welcome to Durdle! The target word has {x} letters')
    num_guess = 0
    while True:
        guess = input('Enter a guess:')
        if len(guess) != x or guess.isalpha() == False or guess.islower() == False:
            print('Invalid guess.')
        else:
            num_guess += 1
            result = durdle_match(guess, target)
            print(" " * 14 + result)
            if result == 'G' * x:
                print(f'Congratulations, you got it in {num_guess} guesses!')
                return num_guess

def get_genes(dna_string):
    '''
    Purpose: To find the genes in a DNA sequence
    Parameters:
        dna_string: an input consisting of A, T, C, and G's that contains genes
    Return Value: A list that contains the gene(s) found in the DNA sequence

    '''
    start = 'ATG'
    stop1 = 'TAG'
    stop2 = 'TAA'
    stop3 = 'TGA'
    genes = []
    i = 0
    j = 0
    while i < len(dna_string):
        if dna_string[i:i+3] == start:
            j = i + 3
            while j < len(dna_string):
                print(dna_string[j:j+3])
                if dna_string[j:j+3] == stop1:
                    gene = dna_string[i+3:j]
                    genes.append(gene)
                    break
                elif dna_string[j:j+3] == stop2:
                    gene = dna_string[i+3:j]
                    genes.append(gene)
                    break
                elif dna_string[j:j+3] == stop3:
                    gene = dna_string[i+3:j]
                    genes.append(gene)
                    break
                else:
                    j += 1
            else:
                i += 1
        i += 1
    return genes

