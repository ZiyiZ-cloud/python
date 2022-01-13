def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    result= phrase.title()
    print(result)
    

titleize('this is awesome')
titleize('oNLy cAPITALIZe fIRSt')