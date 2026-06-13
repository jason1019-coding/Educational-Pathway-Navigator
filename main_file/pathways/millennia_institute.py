millennia_institute_pathways = {
"name": "Millennia Institue (MI)",
 "qualification": "A-Level",
 "duration": "3 years",
 "description": "A pre-university programme that prepares students for the A-Level examinations over 3 years instead of 2.",
 "application_methods": "Joint Admission Exercise [JAE], DSA",
 "eligibility": "Meet an L1R4 of 20 or lower",
 "streams":{
"Arts": {
    "description": "Focuses on humanities, languages, and social sciences.",
    "sujects": [
        "History",
        "Geography",
        "Literature in English",
        "Economics",
        "China Studies in English",
        "Mathematics"
    ]
},
"Science": {
    "description": "Focuses on mathematics and the sciences.",
    "subjects": [
        "Mathematics",
        "Further Mathematics",
        "Physics",
        "Chemistry",
        "Biology",
        "Economics",
    ]
},
"Commerce": {
    "description": "Focuses on business, accounting, and economics.",
    "subjects": [
        "Management of Business",
        "Principal of Accounts",
        "Economcs",
        "Mathematics"
    ]
}
}
}

def millennia_institute():
    import sys

    while True:
        millennia_input = input("Would you like to know about Millennia Institute pathways? (yes/no/exit): ").strip().lower()
        if millennia_input == 'yes':
            while True:
                print("Available pathways:")
                for key, value in millennia_institute_pathways.items():
                    print(f"{key}: {value['name']}")

                millennia_detail_input = input("Which Millennia Institute pathway would you like to know more about? (or 'no' to return to main menu): ").strip()
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
                    print("Pathway not found. Please enter a valid pathway name or 'no' to return to main menu.")

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