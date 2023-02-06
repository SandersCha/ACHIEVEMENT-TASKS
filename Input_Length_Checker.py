while True: # looping until user enters a valid username.

    userName = input("Please enter your uername (Username needs to be longer than one letter): ") # Receive the input of the username from user.
    print("Thank you! Your username is", len(userName), "charactor long.") # Display the length of the userName.

    if len(userName) <= 1: # Set the condition that if the length of the string is less than 1 character.
        print("Sorry, username must be longer than one letter.") # If the user inputs the username with less than 1 character, then print the message.

    elif len(userName) > 20:
        print("Sorry, username cannot be more than 20 letters in length.") # Display error message if more than 20 letters are entered.

    elif userName == userName.lower() or userName.isalpha(): # If user inputs all lower case or no any numbers, will display error message and return to user with the same question.
        print("Sorry, one upper case alphabet and one number 0-9 is needed") # Display error message if the entry is lack of one upper case and one number.

    else:
        break # If the username input by the user is valid, i.e., none of the above conditions matches, then it will display "Thank you" and the length of userName, and stop the program.
