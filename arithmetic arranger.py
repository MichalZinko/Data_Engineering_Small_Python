def arithmetic_arranger(problems, show_answers=False):
#Checking error section

    # Checking if there are too many problems
    amount_of_problmes = len(problems)
    if amount_of_problmes > 5:
        return 'Error: Too many problems.'

    # Checking if there aren't any multiplications and divisions
    problem_number = 0

    upper_number_list = []
    lower_number_list = []
    dashes_list = []
    anwser_list = []

    for equation in problems:
        seperated = equation.split(' ')
        upper_number = seperated[0]
        lower_number = seperated[2]
        operator = seperated[1]

        if operator == '*' or operator == '/':
            return "Error: Operator must be '+' or '-'."

        # Checking if only numbers are used for the equation 
        if upper_number.isdigit() is not True or lower_number.isdigit() is not True:
            return 'Error: Numbers must only contain digits.'

        
        # Checking if numbers are not more than 4 digits  
        upper_number_length = len(upper_number)
        lower_number_length = len(lower_number)

        if upper_number_length > 4 or lower_number_length > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
# Printing equestion numbers section

        if problem_number == 0:
            spaces = 0
        else:
            spaces = 4
        
        equation_width = max(upper_number_length, lower_number_length) + 2

        upper_number_list.append(' ' * (spaces + ( equation_width - upper_number_length)) + upper_number)
        lower_number_list.append(' ' * spaces + operator + ' ' * ( equation_width - lower_number_length  - 1) + lower_number)
        dashes_list.append (' ' * spaces + '-' * equation_width)

        if show_answers == True:
            if operator == '-':
                if int(upper_number) >= int(lower_number):
                    anwser_operator = ' '
                    anwser = int(upper_number) - int(lower_number)
                else:
                    anwser_operator = '-'
                    anwser = int(lower_number) - int(upper_number)
            else:
                anwser_operator = ' '
                anwser = int(upper_number) + int(lower_number)

            anwser_list.append(' ' * spaces + ' ' * (equation_width - len(str(anwser)) - 1)  + anwser_operator +  str(anwser))

        problem_number =+ 1
    
    upper_line = ''.join(upper_number_list)
    lower_line = ''.join(lower_number_list)
    dashes_line = ''.join(dashes_list)
    if show_answers == True:
        anwser_line = ''.join(anwser_list)
        text = "\n".join((upper_line, lower_line, dashes_line, anwser_line))
    else:
        text = "\n".join((upper_line, lower_line, dashes_line))
    return text      

def main_menu():
    equasions = input()
    list = equasions.split(",")
    clean_list = []
    for equasion in list:
        check = equasion.strip()
        clean_equasion = check.split()
        if len(clean_equasion) != 3:
            print("Please make sure there is a space and betwen equasion and operator")
            main_menu()
        else:
            clean_list.append(check)
    return clean_list

def anwser(): 
    print("Input y if yes or n if no")
    anwser = input().lower().strip()
    if anwser == 'y':
        full_view = True
    elif anwser == 'n':
        full_view = False
    else:
        print("Please select a valid option")
        main_menu()
    return full_view

print('~Welcome to arithmetic arranger~')
print('Input your problem and make sure there is a space and betwen equasion and operator and that you seperate equestions with ,')
clean_list = main_menu()
print(clean_list)
print("Do you want to see the anwsers")
full_view = anwser() 

print(f'\n{arithmetic_arranger(clean_list, full_view)}') 