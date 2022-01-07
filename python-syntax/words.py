def print_upper_words(words):
    for word in words.split():
        upper_case= word.upper()
        print(upper_case)
        
        
print_upper_words('this is new')

def start_with_e(words):
    for word in words.split():
        if word[0] == 'e':
            upper_case= word.upper()
            print(upper_case)

start_with_e('this is a elephant')


def start_with_selection(str,selections):
    for words in str:
        for word in words.split():
            for selection in selections:
                if word[0] == selection:
                    upper_case= word.upper()
                    print(upper_case)
            
start_with_selection(["hello", "hey", "goodbye", "yo", "yes"],
                {'y','h'})