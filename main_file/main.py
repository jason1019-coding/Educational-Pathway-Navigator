from pathways.primary_sch import primary_school
from pathways.secondary_sch import secondary_school
from pathways.junior_college import junior_college
from pathways.polytechnic import polytechnic
from pathways.millennia_institute import millennia_institute
# from pathways.ite import ite_school_pathways

pathways = {
    "primary": "Primary School",
    "secondary": "Secondary School",
    "junior_college": "Junior College",
    "jc": "Junior College",        # ← shortform
    "polytechnic": "Polytechnic",
    "poly": "Polytechnic",         # ← shortform
    "millennia_institute": "Millennia Institute",
    "mi": "Millennia Institute",   # ← shortform
}
display_options = [
    "Primary School",
    "Secondary School",
    "Junior College",
    "Polytechnic",
    "Millennia Institute"
]

def user_input():
    while True:
        print("Welcome to Educational Pathway Navigator")
        print("Please select an educational pathway to explore:")
        for option in display_options:
            print(f"  - {option}")
        user_choice = input("What educational pathway are you interested in? (or 'exit' to quit): ")
        if user_choice.lower() in pathways:
            print(f"You have selected the {user_choice.lower()} pathway.")
            if user_choice.lower() == 'primary':
                primary_school()
            elif user_choice.lower() == 'secondary':
                secondary_school()
            elif user_choice.lower() == 'junior' or user_choice.lower() == 'jc' or user_choice.lower() == 'junior_college':
                junior_college()
            elif user_choice.lower() == 'polytechnic' or user_choice.lower() == 'poly':
                polytechnic()
            elif user_choice.lower() == 'millennia_institute'or user_choice.lower() == 'millennia' or user_choice.lower() == 'mi':
                millennia_institute()
            elif user_choice.lower() == 'ite':
                print("ITE pathways coming soon!")
        elif user_choice.lower() == 'exit':
                print("Exiting the program.")
                break
                
        else:
            print("Invalid input. Please enter a valid pathway or 'exit' to quit.")

                    
        # the great wall that protects the functions
user_input()
        