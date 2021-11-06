def permutations(word):
    if len(word) <= 1:
        return [[word]]
        
    perms = []
    
    for i in range(0, len(word)):
        starting_letter = word[i]
        remaining_letters = "".join([letter for letter in word if letter != starting_letter])
        sub_permutations = permutations(remaining_letters)
        
        for permutation in sub_permutations:
            perms.append([starting_letter] + permutation)
            
    return perms
    
   
            
if __name__ == "__main__":
    print(permutations("abc"))
