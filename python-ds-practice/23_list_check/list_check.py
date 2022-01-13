def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """     
    result=all(isinstance(item,list) for item in lst)    
    print(result)
list_check([[1], [2, 3]])
list_check([[1], "nope"])