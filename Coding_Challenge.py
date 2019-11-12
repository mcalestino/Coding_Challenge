import json


# This function opens reads the json file and extracts its components
def reader(file):
    # opens the json file
    with open(file, encoding='utf-8') as data_file:
        j_data = json.loads(data_file.read())
    return j_data


# This function outputs all the possible json data points the user sees separately
# extra functionality, more so for testing purposes
def prompt_output(j_data):

    # List for classNames, class and identifer
    output_list = []
    names = recursed_function(j_data, "classNames")
    classes = recursed_function(j_data, "class")
    identifiers = recursed_function(j_data, "identifier")

    # Conditional statement to go through the names of classes
    # and outputs the list
    for current in classes:
        output_list.append(current)
    for sublist in names:
        for current in sublist:
            output_list.append(current)
    for current in identifiers:
        output_list.append(current)
    print(output_list)
    print("")
    return


# This function looks for relevant data points which
# is based on the selector the user chooses
def recursed_function(j_data, user_input):

    # Decision starement to check if data is list type
    # Recursive statement that checks subgroups that yields matching data points to user input
    if (isinstance(j_data, list)):
        for d_point in j_data:
            for child in recursed_function(d_point, user_input):
                yield child

    # Decision statement to check if data is dictionary type
    # This function recursively checks subgroups and yields matching data points to input
    elif (isinstance(j_data, dict)):
        for c_word, nested_data in j_data.items():
            if c_word == user_input:
                yield nested_data
            for data_point in recursed_function(nested_data, user_input):
                yield data_point

    else:
        return
    return

# This function outputs the json data based on the word given by the user
def prompt(j_data, word):

    output_list = []
    num_class = 0
    output = recursed_function(j_data, word)

    if (word == "classNames"):
        for sublist in output:
            for current in sublist:
                output_list.append(current)

    else:
        for current in output:
            output_list.append(current)
            if current == "Input":
                num_class = num_class + 1

    print(output_list)
    print(" ")

    if (word == "class"):
        print("Number of Classes:",num_class)
        print(" ")
    return

# Main function for which a user is prompted to select a selector
# or exit the program
def main():

    # Used variable cantina_data for the json data
    cantina_data = reader('SystemViewController.json')

    user = "";
    print("Hello!")
    print("Please select the type that you would like to see:")
    print("'class,''classNames', 'identifier', 'all' or enter 'exit' if you wish to end the program.")
    print("")

    # consistently prompt for user input until the user exits
    while user != "exit":

        # Variable to ask the user for their answer
        user = input("Please enter your answer: ")
        user = user.lower()
        print("")

        # Decision statement for selections from user
        if user == "classnames":
            user = "classNames"
            prompt(cantina_data, user)

        elif user == "class":
            prompt(cantina_data, user)

        elif user == "identifier":
            prompt(cantina_data, user)

        elif user == "all":
            prompt_output(cantina_data)

        # Decision statement for user to exit program
        elif user == "exit":
            print("Thank you for choosing")
            print("Have a nice day! :-)")
            break;

        # Decision statement if the user chooses a invalid entry
        else:
            print("Invalid entry. Please try again!")

# Needed for main function
main()
