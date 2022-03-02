'''
   CISC-121 2022W

   This is a Vigenere encryption program. This program asks the user for a key
   and plain text. It than encrypts the plain text given, using the Vigenere table
   and Vigenere encryption technique. The program than displays the non encrypted
   plain text and encrypted plain text to the user.

   Name:   Raif Rizwan Karkal
   Student Number: 20261498
   Email:  20rrk2@queensu.ca

   I confirm that this assignment solution is my own work and conforms to
   Queen's standards of Academic Integrity
'''


def Vigenere_Table():
    """
    This function is responsible for generating the Vigenere table in a form of a list.
    The function creates one large list, in which multiple lists are created that holds the Vigenere
    table's alphabets. The number of lists within the large list indicates the rows while the number of
    alphabets in the list indicates the columns.

    Parameters: None
    Return Value: vigenere_table
     """

    # assigning number 0 to variable row
    row = 0
    # List created with the english Alphabets and assigned to a variable
    Alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    # Empty list assigned to variable vigenere_table
    vigenere_table = []

    # while loop which continues until row variable integer is less than 26 which represent rows in the Vigenere table
    while row < 26:
        # Slicing letters in the alphabet list from 0 to the row number
        sliced_alphabet = Alphabets[0:row]
        # slicing letters from the row number to whatever is left in the list
        remaining_alphabet = Alphabets[row:]
        # concatenating the sliced and remaining alphabet list. This creates a new list hence the variable name
        new_list = remaining_alphabet + sliced_alphabet
        # Appending the vigenere table list with new lists.
        vigenere_table.append(new_list)
        # adding one to the row so the loop stops at 26.
        row += 1

    # returning the vigenere table
    return vigenere_table


def removal_non_letters (plaintext_uppercase):
    """
    This function is responsible for removing all non-letters from the plaintext entered by the user.
    The function converts the plaintext string into a list and goes through each letter, removing any non-letters
    such as special characters, numbers etc.

    Parameters: plaintext_uppercase
    Return Value: only_letters_plaintext_list
     """

    # creating empty list and assigning to only_letter_plaintext_list
    only_letters_plaintext_list = []

    # for loop in which each letter in the string plaintext_uppercase is assigned the variable letter
    for letter in plaintext_uppercase:
        # if statement which checks if each letter is an alphabet. Program continues here if true
        if letter.isalpha():
            # only letters plaintext list appended with letter if alphabet
            only_letters_plaintext_list.append(letter)

    # returning the only letter plaintext list.
    return only_letters_plaintext_list


def encryption_plaintext (key_uppercase, only_letters_plaintext_list, Vigenere_table):
    """
    This function is responsible for encrypting the plaintext. The function first converts the
    key string into a list. The key list is than changed depending on the length of the only letter
    plaintext list. There could be letters added or removed from the key list in order to match the
    the length of the key list and only plaintext list. Once the key list is completed, the encryption
    is proceeded. The encryption process involves reading each letter of the key list and only letter
    plaintext list than applying the Vigenere encryption by looking through the Vigenere table for the
    letters to convert each letter in the only letter plaintext list too.

    Parameters: key_uppercase, only_letters_plaintext_list, Vigenere_table
    Return Value: encrypted_plaintext_list
     """

    # empty list assigned to encrypted plaintext list and key list
    encrypted_plaintext_list = []
    key_list = []

    # for loop in which each letter in key_uppercase is assigned to variable key_letter
    for key_letters in key_uppercase:
        # appending key list with each key letter
        key_list.append(key_letters)

    # finding the difference between the length of the list only letter plaintext list and key list. Used for encryption
    difference = int(len(only_letters_plaintext_list)) - int(len(key_list))

    # if length of the key list and only letter plaintext list and no equal, program continues here
    if len(key_list) != len(only_letters_plaintext_list):
        # if length of key list is less than only letter plaintext list, program continues here
        if len(key_list) < len(only_letters_plaintext_list):
            # for loop in which variable num assigned to each number in range from 0 to the difference variable
            for num in range(difference):
                # key list appended with specific letters within the same list which is determined by the num variable
                key_list.append(key_list[num])

        # if the length of the key list is greater than only letter plaintext list, program continues here
        elif len(key_list) > len(only_letters_plaintext_list):
            # for loop in which variable num2 assigned to each number from 0 to difference times -1. The -1 is included for a positive number in range function
            for num2 in range(-1 * difference):
                # key list pop function used to remove the last letter in the list. This continues until the loop is completed.
                key_list.pop(-1)

    # for loop in which variable x assigned to each number from 0 to the length of only letter plaintext list
    for x in range (len(only_letters_plaintext_list)):
        # row variable used to hold the difference in ord value of each letter in the key list and the ord of A
        row = ((ord(key_list[x]) - ord("A")))
        # column variable used to hold the difference in ord value of each letter in the only letter plaintext list and the ord of A
        column = ((ord(only_letters_plaintext_list[x]) - ord("A")))
        # using the row and column variable to generate a specifc vigenere encryption letter from the vigenere table
        letter = Vigenere_table[row][column]
        # appending the encrypted plaintext list with each letter generated
        encrypted_plaintext_list.append(letter)

    # returning the encrypted plaintext list
    return encrypted_plaintext_list


def main():
    """
    The main function controls the program flow. This is where execution will start. The main function
    also holds the user interface that is displayed to the user. Furthermore, different
    functions are called from the main function.

    Parameters:
    Return Value:
     """

    # Getting input from the user - plaintext and key
    print ("Vigenere Encryption \n")
    plaintext_input = input("Please enter the plain text: ")
    key_input = input("Please enter a key to be used: ")

    # Converting plaintext and key to all uppercase letters
    plaintext_uppercase = plaintext_input.upper()
    key_uppercase = key_input.upper()

    # Calling Vigenere_table function in order to generate the vigenere table. Result saved to Vigenere_table variable
    Vigenere_table = Vigenere_Table()
    # Calling removal non letters function with plaintext_uppercase as parameter. The result saved to only_letter_plaintext_list variable
    only_letters_plaintext_list = removal_non_letters(plaintext_uppercase)
    # Calling encryption plaintext function with key_uppercase, only_letter_plaintext_list and vigenere_table as parameter.
    encrypted_plaintext_list = encryption_plaintext(key_uppercase, only_letters_plaintext_list, Vigenere_table)

    # Assigning empty string to non_encrypted_plaintext and encrypted_plaintext
    non_encrypted_plaintext = ""
    encrypted_plaintext = ""

    # for loop in which variable letter assigned to each letter in the only letters plaintext list
    for letter in only_letters_plaintext_list:
        # each letter in the list added to non_encrypted_plaintext string
        non_encrypted_plaintext += letter

    # for loop in which variable letter assigned to each letter in the encrypted_plaintext_list
    for letter in encrypted_plaintext_list:
        # each letter in the list added to non_encrypted_plaintext string
        encrypted_plaintext += letter

    # Displaying the result of the encryption for the user. Showing both non encrypted and encrypted
    print("Non-encrypted plain text:",non_encrypted_plaintext)
    print("Encrypted plain text:",encrypted_plaintext)


# Calling main function in order to run the program
main()

