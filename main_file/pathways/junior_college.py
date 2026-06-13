junior_college_pathways = {
    "A Level": {
        "name": "A Level",
        "description": "A 2-year programme that involves the suffering of countless 17 and 18 year olds.",
        "deadline": "Typically in the second half of the year, between September and November",
        "eligibility": "For secondary school students who can study and are willing to subject themselves to the depths of academic horror"
        },
    "IB": {
        "name": "International Baccalaureate (IB)",
        "description": "A 2-year programme that involves multiple side projects, such as Internal Assessments and the Extended Essay. There is also a strong focus on extracurricular activties via the Creativity, Activity, Service (CAS) component.",
        "deadline": "Typically in the second half of the year, between September and November",
        "eligibility": "Open to both international and local students. Students that can juggle multiple projects and can still study hard enough for the (admittedly MUCH less grindy than A-levels) final exams."
    }
}

def junior_college():
    import sys

    while True:
        junior_college_input = input("Would you like to know about junior college pathways? (yes/no/exit): ").strip().lower()
        if junior_college_input == 'yes':
            while True:
                print("Available pathways:")
                for key, value in junior_college_pathways.items():
                    print(f"{key}: {value['name']}")

                junior_college_detail_input = input("Which junior college pathway would you like to know more about? (or 'no' to return to main menu): ").strip()
                if junior_college_detail_input.lower() == 'no':
                    print("No problem! Returning to main menu.")
                    return
                if junior_college_detail_input.lower() == 'exit':
                    sys.exit()

                found = False
                for key, value in junior_college_pathways.items():
                    if junior_college_detail_input.lower() == key.lower():
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
                    junior_college_another_input = input("Would you like to know about another pathway? (yes/no/exit): ").strip().lower()
                    if junior_college_another_input == 'yes':
                        break
                    elif junior_college_another_input == 'no':
                        print("No problem! Returning to main menu.")
                        return
                    elif junior_college_another_input == 'exit':
                        sys.exit()
                    else:
                        print("Please enter yes, no, or exit.")
            continue
        elif junior_college_input == 'no':
            print("No problem! Returning to main menu.")
            break
        elif junior_college_input == 'exit':
            sys.exit()
        else:
            print("Please enter yes, no, or exit.")