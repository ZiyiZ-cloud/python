def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    result1={}
    result2={}
    list1=[int(i) for i in str(num1)]
    list2=[int(i) for i in str(num2)]
    for num in set(list1):
        result1[num]=list1.count(num)
    for num in set(list2):
        result2[num]=list2.count(num)
    if result1==result2:
        print(True)
    else:
        print(False)
        

same_frequency(551122, 221515)
same_frequency(321142, 3212215)
same_frequency(1212, 2211)
