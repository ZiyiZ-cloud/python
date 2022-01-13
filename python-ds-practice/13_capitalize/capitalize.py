def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    if phrase[0].isupper():
        print(phrase)
    if phrase[0].islower():
        print(phrase.capitalize())


capitalize('python')
capitalize('only first word')