def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    true_lst=[]
    false_lst=[0,0.0,'',None,False,[],{},set(),()]
    for item in lst:
        if item not in false_lst:
            true_lst.append(item)
    print(true_lst)
    
compact([0, 1, 2, '', [], False, (), None, 'All done'])