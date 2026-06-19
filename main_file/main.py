import os
from pathways.primary_sch import primary_school
from pathways.secondary_sch import secondary_school
from pathways.junior_college import junior_college
from pathways.polytechnic import polytechnic
from pathways.millennia_institute import millennia_institute
# from pathways.ite import ite_school_pathways

# Updated to look up selection by numbers
pathways = {
    "1": "Primary School",
    "2": "Secondary School",
    "3": "Junior College",
    "4": "Polytechnic",
    "5": "Millennia Institute"
}

display_options = [
    "[1] Primary School",
    "[2] Secondary School",
    "[3] Junior College",
    "[4] Polytechnic",
    "[5] Millennia Institute"
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def user_input():
    while True:
        clear_screen()
        
        print("Welcome to Educational Pathway Navigator")
        print("Please select an educational pathway to explore:")
        for option in display_options:
            print(f"  {option}")
            
        user_choice = input("\nWhat educational pathway are you interested in? Enter number (1-5) or 'exit' to quit: ").strip()
        
        if user_choice in pathways:
            selected_pathway = pathways[user_choice]
            print(f"\nYou have selected the {selected_pathway} pathway.\n")
            
            if user_choice == '1':
                primary_school()
            elif user_choice == '2':
                secondary_school()
            elif user_choice == '3':
                junior_college()
            elif user_choice == '4':
                polytechnic()
            elif user_choice == '5':
                millennia_institute()
                
            input("\nPress Enter to go back to the menu...")

        elif user_choice.lower() == 'exit':
            print("Exiting the program.")
            break
                
        else:
            print("\nInvalid input. Please enter a number from 1 to 5, or 'exit' to quit.")
            input("\nPress Enter to try again...")

# the great wall that protects the functions
user_input()