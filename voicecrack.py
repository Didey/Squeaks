import os, glob
from datetime import datetime

# Indexes and displays the names of all the people who's squeaks have been documented in the past.
def show_past_kids():
    print("Here's the names of all the kid's who have squeaked before:")
    os.chdir("./")
    for file in glob.glob("*.txt"):
        print(os.path.splitext(file)[0])
    check_name()

# Checks if the name of the squeakee has been used before, and creates a new text file if it hasn't.
def check_name():
    squeaker = raw_input("What's the name of the kid who squeaked?\n")
    if not os.path.isfile("{}.txt".format(squeaker)):
        print("Not a file. Creating file {}.txt...".format(squeaker))
        new_squeak = open("{}.txt".format(squeaker), 'w+')
        write_squeak(squeaker)
    else:
        write_squeak(squeaker)
# Uses the name of the squeaker retrived from check_name to write squeak info to the already made txt file. 
def write_squeak(squeaker):
    curr_time = datetime.now().strftime("%H:%M:%S")
    curr_date = datetime.now().strftime("%m/%d/%Y")
    cracked = raw_input("What did the kid say?\n")
    with open("{}.txt".format(squeaker), "a") as squeak_fl:
        squeak_fl.write("{} squeaked saying \"{}\" at {} on {}.\n\n".format(squeaker, cracked, curr_time, curr_date))
    print("Squeak documented, what a loser.")
    
        


if __name__ == '__main__':
    show_past_kids()
