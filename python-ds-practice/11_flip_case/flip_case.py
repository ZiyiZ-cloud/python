def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # p_list = list(phrase)
    # c =to_swap.casefold()
    # up = c.upper()
    
    # for l in p_list:
    #     if l == c or up:
    #         if l.islower():
    #             l.upper()
    #         if l.isupper():
    #             l.lower()
                
    # new_phrase=''.join(p_list)
    # print(new_phrase)
    
    
    phrase = list(phrase)
    print(phrase)
    length = len(phrase)
    j = 0 
    
    to_swap = to_swap.casefold()
    to_swap_up = to_swap.upper()
    
    while j < length:
        curr = phrase[j]
        
        if curr == to_swap:
            phrase[j] = to_swap_up
        if curr == to_swap_up:
            phrase[j] = to_swap
        
        j += 1
    
    new_phrase = ''.join(phrase)
    
    print(new_phrase)
    
    return new_phrase
    
    
            
    
flip_case('Aaaahhh', 'a')
flip_case('Aaaahhh', 'A')
flip_case('Aaaahhh', 'h')