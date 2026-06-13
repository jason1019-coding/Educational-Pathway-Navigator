secondary_sch_pathways = {
    "Junior College/IB Program": { 
        "name": "Junior College/IB Program",
        "description": "A 2-year program that prepares students for university education, culminating in    the GCE A-Level or International Baccalaureate (IB) examinations.",
        "eligibility": "The Metric: L1R4 (Language + 4 Relevant Subjects), All subjects used for this calculation must be taken at the most demanding academic level (G3)."
    },

    "Polytechnic Foundation Programme (PFP)": {
        "name": "Polytechnic Foundation Programme (PFP)",
        "description": "A 1-year program that provides an alternative pathway for students to enter polytechnic education.",
        "eligibility": "Because spaces are limited, students generally need to score mostly Grade 1s and 2s in their G2 subjects to successfully secure a spot in popular polytechnic courses."

    },
    "Millennia Institute (MI)": {
        "name": "Millennia Institute (MI)",
        "description": "A 3-year program that offers a more flexible curriculum and allows students to take a combination of academic and vocational subjects.",
        "eligibility": "Grade Cut-off: A gross aggregate score of 20 points or fewer, Like JCs, subjects must be offered at the G3 level, but the slightly wider threshold accommodates students who may have experienced a minor slip in one or two subjects."
    },
    
    "Polytechnic Diplomas (Direct Entry to Year 1)": {
        "name": "Polytechnic Diplomas",
        "description": "Students can directly enter the first year of polytechnic education based on their GCE O-Level results.",
        "eligibility": "Grade Cut-off: Typically requires a gross aggregate score of around 12 points or fewer, with strong performance in relevant subjects. The exact cut-off can vary by polytechnic and course, but generally, students need to excel in their G2 subjects to secure direct entry into competitive diploma programs."
    },
    "ITE 2-Year Higher Nitec Program": {
        "name": "ITE 2-Year Higher Nitec Program",
        "description": "A 2-year program that provides specialized training in various technical and vocational fields.",
        "eligibility": "Students typically need to have completed their GCE O-Level examinations with a minimum aggregate score, and may need to pass an entrance examination or interview."    
    },
    "ITE 3-Year Higher Nitec Program": {   
        "name": "ITE 3-Year Higher Nitec Program",
        "description": "A 3-year program that offers more in-depth training and specialization in technical and vocational fields.",
        "eligibility": "Students typically need to have completed their GCE O-Level examinations with a minimum aggregate score, and may need to pass an entrance examination or interview."
    },
    "Arts Institutions (NAFA & LASALLE Diplomas)": {
        "name": "Arts Institutions (NAFA & LASALLE Diplomas)",
        "description": "Specialized arts programs that offer comprehensive training in various artistic disciplines.",
        "eligibility": "Admission is typically based on portfolio review, interviews, and academic performance."
    }
}

def secondary_school():
    import sys

    while True:
        secondary_sch_input = input("Would you like to know about secondary school pathways? (yes/no/exit): ").strip().lower()
        if secondary_sch_input == 'yes':
            while True:
                print("Available pathways:")
                for key, value in secondary_sch_pathways.items():
                    print(f"{key}: {value['name']}")

                secondary_sch_detail_input = input("Which secondary school pathway would you like to know more about? (or 'no' to return to main menu): ").strip()
                if secondary_sch_detail_input.lower() == 'no':
                    print("No problem! Returning to main menu.")
                    return
                if secondary_sch_detail_input.lower() == 'exit':
                    sys.exit()

                found = False
                for key, value in secondary_sch_pathways.items():
                    if secondary_sch_detail_input.lower() == key.lower():
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
                    secondary_sch_another_input = input("Would you like to know about another pathway? (yes/no/exit): ").strip().lower()
                    if secondary_sch_another_input == 'yes':
                        break
                    elif secondary_sch_another_input == 'no':
                        print("No problem! Returning to main menu.")
                        return
                    elif secondary_sch_another_input == 'exit':
                        sys.exit()
                    else:
                        print("Please enter yes, no, or exit.")
            continue
        elif secondary_sch_input == 'no':
            print("No problem! Returning to main menu.")
            break
        elif secondary_sch_input == 'exit':
            sys.exit()
        else:
            print("Please enter yes, no, or exit.")