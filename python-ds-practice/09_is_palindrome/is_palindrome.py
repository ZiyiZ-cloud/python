def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    case_fold=phrase.casefold()
    no_space=case_fold.replace(' ','')
    List= list(no_space)
    old_list=List.copy()
    List.reverse()
    if List == old_list:
        print(True)
    else:
        print(False)
        

is_palindrome('tacocat')
is_palindrome('noon')
is_palindrome('robert')
is_palindrome('taco cat')
is_palindrome('Noon')