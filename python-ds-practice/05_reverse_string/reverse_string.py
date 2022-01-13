def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    List=list(phrase)
    List.reverse()
    print(''.join(List))
    
    
reverse_string('awesome')
reverse_string('sauce')