millennia_institute_pathways = {
    "Arts": {
        "name": "Arts Stream",
        "description": "Focuses on humanities, languages, and social sciences.",
        "eligibility": "Meet an L1R4 of 20 or lower",
        "subjects": ["History", "Geography", "Literature in English"]
    },
    "Science": {
        "name": "Science Stream",
        "description": "Focuses on mathematics and the sciences.",
        "eligibility": "Meet an L1R4 of 20 or lower",
        "subjects": ["Mathematics", "Physics", "Chemistry"]
    },
    "Commerce": {
        "name": "Commerce Stream",
        "description": "Focuses on business, accounting, and economics.",
        "eligibility": "Meet an L1R4 of 20 or lower",
        "subjects": ["Management of Business", "Economics", "Mathematics"]
    }
}

display_options = {
    "Arts": "Arts Stream",
    "Science": "Science Stream",
    "Commerce": "Commerce Stream"
}

def millennia_institute():
    import sys

    while True:
        millennia_input = input("Would you like to know about Millennia Institute pathways? (yes/no/exit): ").strip().lower()
        if millennia_input == 'yes':
            while True:
                print("Available pathways:")
                for key, value in display_options.items():
                    print(f"{key}: {value}")

                millennia_detail_input = input("Which Millennia Institute pathway would you like to know more about? (input in short form) (or 'no' to return to main menu): ").strip()
                if millennia_detail_input.lower() == 'no':
                    print("No problem! Returning to main menu.")
                    return
                if millennia_detail_input.lower() == 'exit':
                    sys.exit()

                found = False
                for key, value in millennia_institute_pathways.items():
                    if millennia_detail_input.lower() == key.lower():
                        print(f"Name: {value['name']}")
                        print(f"Description: {value['description']}")
                        print(f"Eligibility: {value['eligibility']}")
                        if 'deadline' in value:
                            print(f"Deadline: {value['deadline']}")
                        found = True
                        break

                if not found:
                    print("Pathway not found. Please enter a valid pathway name in short form or 'no' to return to main menu.")

                while True:
                    millennia_another_input = input("Would you like to know about another pathway? (yes/no/exit): ").strip().lower()
                    if millennia_another_input == 'yes':
                        break
                    elif millennia_another_input == 'no':
                        print("No problem! Returning to main menu.")
                        return
                    elif millennia_another_input == 'exit':
                        sys.exit()
                    else:
                        print("Please enter yes, no, or exit.")
            continue
        elif millennia_input == 'no':
            print("No problem! Returning to main menu.")
            break
        elif millennia_input == 'exit':
            sys.exit()
        else:
            print("Please enter yes, no, or exit.")