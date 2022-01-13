def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    num_dic={}
    nums_set=set(nums)
    for num_set in nums_set:
        num_count = nums.count(num_set)
        num_dic[num_set]=num_count
    print(max(num_dic,key=num_dic.get))
        
        

        


mode([1, 2, 1])
mode([2, 2, 3, 3, 2])