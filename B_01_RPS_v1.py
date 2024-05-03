import random

# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=("yes", "no")):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()


# outputs instructions
def instructions():
    print('''


**** Instructions ****

To begin, choose the number of rounds (or press <enter> for
infinite mode).

Then play against the computer. You need to choose R (rock), P (paper) or S (scissors).

The rules are as follows:
 -> Rock beats Scissors
 -> Scissors beats Paper
 -> Paper beats Rock.

Type [xxx] to end the game at anytime you'd like.

Good Luck!
    ''')


# checks for an integer more than 0 (allows <enter>)
def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks that the number is more than / equal to 13
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# compares user / computer choice and returns
# result (win / loss / tie)
def rps_compare(user, comp):

    # if user and computer are the same, game ends with tie
    if user == comp:
        result = "tie"

    # three ways to win
    elif user == "paper" and comp == "rock":
        result = "win"
    elif user == "rock" and comp == "scissors":
        result = "win"
    elif user == "scissors" and comp == "paper":
        result = "win"

    # if not a win or tie = loss
    else:
        result = "lose"

    return result


# main routine

# startup game variables
mode = "regular"
rounds_played = 0

rps_list = ["rock", "paper", "scissors", "xxx"]

print("🪨 Rock! 🧻 Paper! ✂️ Scissors! 🏁")
print()

# ask user if they want to see the instructions and display
# them if requested
want_instructions = string_checker("Would you like to read the instructions?")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()
# ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# game loop starts here
while rounds_played < num_rounds:

    # rounds headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\n♾~♾ Round {rounds_played + 1} (Infinite Mode) ♾~♾"
    else:
        rounds_heading = f"\n Round {rounds_played + 1} of {num_rounds}!"

    print(rounds_heading)


    # random choice from rps_list (without exit code)
    comp_choice = random.choice(rps_list[:-1])
    print("Computer choice", comp_choice)

    # get user choice
    user_choice = string_checker("Choose:", rps_list)
    print("You chose:", user_choice)

    # if user choice is exit code, break the loop
    if user_choice == "xxx":
        break

    result = rps_compare(user_choice, comp_choice)
    print(f"{user_choice} vs {comp_choice}, {result}")

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1

# game loop ends here

# game history / statistics
