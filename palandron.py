
print('Palandron Tester')

def main_menu():
    print('Input the word that you want to check')
    test = input()
    return test

def palindrom(word):
    starting_letter_index = 0
    ending_letter_index  = -1
    half_of_lenght_of_word = int(len(word) / 2 + len(word) % 2)
    while starting_letter_index <= half_of_lenght_of_word:
        if starting_letter_index == half_of_lenght_of_word:
            return print("This is a Palindrom")
        else:
            if word[starting_letter_index] != word[ending_letter_index]:
                return print("This is not a Palindrom")
        starting_letter_index += 1
        ending_letter_index -= 1

word = main_menu()
palindrom(word)
