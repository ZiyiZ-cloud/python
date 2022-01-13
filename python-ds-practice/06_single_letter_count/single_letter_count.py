def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    Fold= word.casefold()
    Count=Fold.count(letter)
    print(Count)



single_letter_count('Hello World', 'h')
single_letter_count('Hello World', 'z')
single_letter_count("Hello World", 'l')