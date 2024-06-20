
def main_menu():
    print('\nInput the word that you want to check')
    user_input = input()
    return user_input
    
def palindrom(word):
    starting_letter_index = 0
    ending_letter_index  = -1
    half_of_lenght_of_word = int(len(word) / 2 + len(word) % 2)
    while starting_letter_index <= half_of_lenght_of_word:
        if starting_letter_index == half_of_lenght_of_word:
            return print("\nThis is a Palindrom")
        else:
            if word[starting_letter_index] != word[ending_letter_index]:
                return print("\nThis is not a Palindrom")
        starting_letter_index += 1
        ending_letter_index -= 1

def ending():
    print('\nDo you want check another word')
    print('If Yes press y if No press n')
    anwser = input()
    if anwser.lower() == 'y':
        order()
    elif anwser.lower() == 'n':
        exit 
    else:
        print('That is not a valid option')
        ending() 

def order():
    user_input_word = main_menu()
    palindrom(user_input_word.lower())
    ending()

print('\n~~Palandron Tester~~')
order()