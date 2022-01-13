def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels=['a','e','i','o','u']
    result={}
    foldcase=phrase.casefold()
    phrase_list=list(foldcase)
    
    for element in phrase_list:
        if element in vowels:
            count_vowel=phrase_list.count(element)
            result[f'{element}']=count_vowel
    print(result)
    
vowel_count('rithm school')
vowel_count('HOW ARE YOU? i am great!') 