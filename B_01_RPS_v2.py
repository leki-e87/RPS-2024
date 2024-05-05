import random


# Check that users have entered a valid
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("You did not choose a valid response")


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
        round_result = "tie"

    # three ways to win
    elif user == "paper" and comp == "rock":
        round_result = "win"
    elif user == "rock" and comp == "scissors":
        round_result = "win"
    elif user == "scissors" and comp == "paper":
        round_result = "win"

    # if not a win or tie = loss
    else:
        round_result = "lose"

    return round_result


# main routine

# startup game variables
mode = "regular"

rounds_played = 0
rounds_tied = 0
rounds_lost = 0

rps_list = ["rock", "paper", "scissors", "xxx"]
game_history = []

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
    # adjust game test / game tied counters and add results to game history
    result = rps_compare(user_choice, comp_choice)

    if result == "tie":
        rounds_tied += 1
        feedback = "You're tied!"
    elif result == "lose":
        rounds_lost += 1
        feedback = "You lost... try again!"
    else:
        feedback = "Good job, you won! Have another go!"

    # set up round feedback and output it (user)
    # add it to game history list (include round number)
    round_feedback = f"{user_choice} vs {comp_choice}, {feedback}"
    history_item = f"Round {rounds_played + 1} - {feedback}"

    print(round_feedback)
    game_history.append(history_item)

    rounds_played = rounds_played + 1

    # if users are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1

# game loop ends here

# calculate statistics
if rounds_played > 0:

    rounds_won = rounds_played - rounds_tied - rounds_lost
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100
    percent_tied = 100 - percent_won - percent_lost

# game stats
    print("~~~ GAME STATS ~~~")
    print(f" Won: {percent_won:.2f} \t "
          f" Lost: {percent_lost:.2f} \t "
          f" Tied: {percent_tied:.2f}")

# game history / statistics
show_history = yes_no("Would you like to see the game history?: ")
if show_history == "yes":
    print("\n ⏳ Game History ⏳")

    for item in game_history:
        print(item)
        # print(round_feedback)

if show_history == "no":
    print("✂️ Thank you for playing my version of Rock, Paper, Scissors! ✂️")
    print()
if rounds_played == 0 and show_history == "yes":
    print("ah you left before the game started mate, there's your history")
