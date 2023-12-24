import random
from time import sleep
from os import system
from argparse import ArgumentParser

def snow_spaces(h, i):
    # Calculating spaces by the height of Christmas Tree
        for j in range(h - i):
            if random.random() < 0.1:
                print('\033[37m*', end="")
            
            else:
                print(" ", end="")

def ChristmasTree(y, h):
    """
        \033[1; 31m: Bright Red
        \033[1; 32m: Bright Green
        \033[33m: Yellow
        \033[34m: Bright Blue
        \033[36m: Bright Cyan
        \033[37m: White
    """
    colors = ['\033[31m', '\033[33m', '\033[34m', '\033[36m']
    
    before = h - h // 4         # On the left of the tree
    after = h + h // 4          # On the right of the tree
    
    print("\t\t" + " "* (before + 2) + random.choice(colors) + "MERRY CHIRSTMAS " + y + "\n")
    for i in range(h):
        # Display the Christmas Tree in the middle of Terminal
        print('\t\t\t', end="")
        snow_spaces(h, i)

        # Calculating number of asterisks by the line number of Christmas Tree
        for j in range(2 * i + 1):
            # Print yellow star on the top
            if i == 0:
                print(colors[1], end="")

            # Print the green tree and random led lights
            else:
                # led lights
                if random.random() < 0.2:
                    color = random.choice(colors)
                    print(color, end="")
                
                # Green tree
                else:
                    print("\033[1;32m", end="")
            # Print asterisks to display Tree.
            print("*", end="")
        snow_spaces(h, i)
        # New line
        print()
    
    # Print the trunk of Christmas Tree
    print('\033[37m', end="")
    print("\t\t\t" + " "* (before) + "|" + "|" * (after - before - 1) + "|")
    print("\t\t\t" + " "* before + "|" + "|" * (after - before - 1) + "|")
    print("\t\t\t" +" "* before + "|" + "|" * (after - before - 1) + "|")
    print("\t\t\t" +" "* before + "|" + "|" * (after - before - 1) + "|")
    print("\t\t\t" +" "* before + "|" + "-" * (after - before - 1) + "|")


parser = ArgumentParser()
# height
parser.add_argument("-H", "--height", 
                    type=int,
                    help= "Height of Christmas Tree, height must be Greater than 15 and Less than 26")

# year
parser.add_argument("-y", "--year",
                    type=int,
                    help="Year, must be Greater than 1999 and Less than 3001")

args = parser.parse_args()

if args.height < 15 or args.height > 25 or args.year < 2000 or args.year > 3000:
    parser.error("Invalid value, please try again!!!")

while(True):
    ChristmasTree(str(args.year), args.height)
    sleep(0.5)
    # Delete the displayed previous Tree
    system('cls')