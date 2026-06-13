from pathways.primary_sch import primary_school, primary_school_pathways
from pathways.secondary_sch import secondary_sch_pathways
from pathways.junior_college import junior_college_pathways
from pathways.polytechnic import polytechnic_school_pathways
from pathways.millennia_institute import millennia_institute_pathways
# from pathways.ite import ite_school_pathways

pathways = {
    "primary": primary_school_pathways,
    "secondary": secondary_sch_pathways,
    "junior_college": junior_college_pathways,
    "polytechnic": polytechnic_school_pathways,
    "millennia_institute": millennia_institute_pathways,
    # "ite": ite_school_pathways
}

def user_input():
    while True:
        try:
            print("Welcome to Educational Pathway Navigator")
            print("Please select an educational pathway to explore:")
            for key, value in pathways.items():
                    print(f"{key}")
            user_choice = input("What educational pathway are you interested in? (or 'exit' to quit): ")
            if user_choice.lower() in pathways:
                    if user_choice.lower() == key:
                        print(f"You have selected the {value['name']} pathway.")
                    if user_choice.lower() == 'primary':
                        primary_school()
                    if user_choice.lower() == 'secondary':
                        print("Secondary school pathways coming soon!")
                    if user_choice.lower() == 'junior_college':
                        print("Junior college pathways coming soon!")
                    if user_choice.lower() == 'polytechnic':
                        print("Polytechnic pathways coming soon!") 
                    if user_choice.lower() == 'ite':
                        print("ITE pathways coming soon!")
                
                    
            
            if user_choice.lower() == 'exit':
                print("Exiting the program.")
                break

        except ValueError:
            print("Invalid input. Please enter a valid pathway or 'exit' to quit.")
            user_input()
# the great wall that protects the functions
user_input()
        