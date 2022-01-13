def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """
    full_name=[]
    for element in people:
        first_name=element.get('first')
        last_name=element.get('last')
        full_name.append(f'{first_name} {last_name}')
    print(full_name) 
       
names = [
{'first': 'Ada', 'last': 'Lovelace'},
{'first': 'Grace', 'last': 'Hopper'},
]
extract_full_names(names)