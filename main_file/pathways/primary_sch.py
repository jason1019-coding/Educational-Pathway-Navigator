primary_school_pathways = {
    "DSA": {
        "name": "Direct School Admission",
        "description": "Allows students to apply to secondary schools based on their talents and interests.",
        "deadline": "Typically in the first half of the year",
        "eligibility": "Primary school students with exceptional talents in areas such as sports, arts, or academics."
    },
    "Mainstream": {
        "name": "Mainstream Secondary Pathway",
        "description": "Students follow the standard curriculum and are assessed through national exams.",
        "eligibility": "Primary school students who meet the academic requirements for secondary school admission."
    },
    "IP": {
        "name": "The Integrated Programme (IP) Pathway",
        "description": "A 6-year program that combines the primary and secondary school curricula.",
        "deadline": "Typically in the first half of the year",
        "eligibility": "Primary school students who meet the academic requirements for the IP program."
    },
    "SSIS": {
        "name": "Specialised & Specialised Independent Schools Pathway",
        "description": "Offers specialized education in areas such as arts, sports, or science.",
        "eligibility": "Primary school students with exceptional talents in specific areas who meet the admission requirements."
    }
}

display_options = {
    "Direct School Admission (DSA)": "Direct School Admission",
    "Mainstream Secondary Pathway (mainstream)": "Mainstream Secondary Pathway",
    "The Integrated Programme (IP) Pathway": "The Integrated Programme (IP) Pathway",
    "Specialised & Specialised Independent School (SSIS)": "Specialised & Specialised Independent Schools Pathway"
}
def primary_school():
    import sys

    while True:
        primary_sch_input = input("Would you like to know about primary school pathways? (yes/no/exit): ").strip().lower()
        if primary_sch_input == 'yes':
            while True:
                print("Available pathways:")
                for key, value in display_options.items():
                    print(f"{key}: {value}")

                primary_sch_detail_input = input("Which primary school pathway would you like to know more about? Please type in short form (or 'no' to return to main menu): ").strip()
                if primary_sch_detail_input.lower() == 'no':
                    print("No problem! Returning to main menu.")
                    return
                if primary_sch_detail_input.lower() == 'exit':
                    sys.exit()

                found = False
                for key, value in primary_school_pathways.items():
                    if primary_sch_detail_input.lower() == key.lower():
                        print(f"Name: {value['name']}")
                        print(f"Description: {value['description']}")
                        print(f"Eligibility: {value['eligibility']}")
                        if 'deadline' in value:
                            print(f"Deadline: {value['deadline']}")
                        found = True
                        break

                if not found:
                    print("Pathway not found. Please enter a valid pathway name in shortform or 'no' to return to main menu.")

                while True:
                    primary_sch_another_input = input("Would you like to know about another pathway? (yes/no/exit): ").strip().lower()
                    if primary_sch_another_input == 'yes':
                        break
                    elif primary_sch_another_input == 'no':
                        print("No problem! Returning to main menu.")
                        return
                    elif primary_sch_another_input == 'exit':
                        sys.exit()
                    else:
                        print("Please enter yes, no, or exit.")
            continue
        elif primary_sch_input == 'no':
            print("No problem! Returning to main menu.")
            break
        elif primary_sch_input == 'exit':
            sys.exit()
        else:
            print("Please enter yes, no, or exit.")

        