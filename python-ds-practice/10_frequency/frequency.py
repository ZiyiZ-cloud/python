def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    frequence=lst.count(search_term)
    print(frequence)
    
frequency([1, 4, 3, 4, 4], 4)
frequency([1, 4, 3], 7)