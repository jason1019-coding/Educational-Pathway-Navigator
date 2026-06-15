polytechnic_school_pathways = {
  "LU": {
    "name": "Local Autonomous Universities Pathway",
    "description": "Pursue a full-time undergraduate degree at a government-funded university.",
    "eligibility": "Polytechnic graduates with a competitive Grade Point Average (GPA) and a relevant diploma, subject to university-specific admission criteria."
  },
  "PD": {
    "name": "SkillsFuture Work-Study Post-Diploma Pathway",
    "description": "A work-study program that allows fresh graduates to secure a full-time job while pursuing a post-diploma qualification.",
    "eligibility": "Citizens or Permanent Residents who are within three years of graduation or their Operationally Ready Date (ORD)."
  },
  "Job": {
    "name": "Direct Employment Pathway",
    "description": "Enter the workforce immediately to gain practical industry experience and build professional networks.",
    "eligibility": "All polytechnic graduates holding a valid diploma."
  },
  "SAD": {
    "name": "Specialist & Advanced Diploma Pathway",
    "description": "Deepen industry-specific skills and knowledge through targeted post-diploma courses.",
    "eligibility": "Polytechnic graduates, typically requiring relevant working experience depending on the specific course requirements."
  },
  "POU": {
    "name": "Private & Overseas Universities Pathway",
    "description": "Further academic studies by obtaining a degree from a private education institution or an overseas university.",
    "eligibility": "Polytechnic graduates who meet the academic and financial requirements of the respective target institution."
  }
}
display_options = {
    "LU": "Local Autonomous Universities Pathway",
    "PD": "SkillsFuture Work-Study Post-Diploma Pathway",
    "Job": "Direct Employment Pathway",
    "SAD": "Specialist & Advanced Diploma Pathway",
    "POU": "Private & Overseas Universities Pathway"
}

def polytechnic():
    import sys

    while True:
        polytechnic_input = input("Would you like to know about polytechnic pathways? (yes/no/exit): ").strip().lower()
        if polytechnic_input == 'yes':
            while True:
                print("Available pathways:")
                for key, value in display_options.items():
                    print(f"{key}: {value}")

                polytechnic_detail_input = input("Which polytechnic pathway would you like to know more about? (input in short form) (or 'no' to return to main menu): ").strip()
                if polytechnic_detail_input.lower() == 'no':
                    print("No problem! Returning to main menu.")
                    return
                if polytechnic_detail_input.lower() == 'exit':
                    sys.exit()

                found = False
                for key, value in polytechnic_school_pathways.items():
                    if polytechnic_detail_input.lower() == key.lower():
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
                    polytechnic_another_input = input("Would you like to know about another pathway? (yes/no/exit): ").strip().lower()
                    if polytechnic_another_input == 'yes':
                        break
                    elif polytechnic_another_input == 'no':
                        print("No problem! Returning to main menu.")
                        return
                    elif polytechnic_another_input == 'exit':
                        sys.exit()
                    else:
                        print("Please enter yes, no, or exit.")
            continue
        elif polytechnic_input == 'no':
            print("No problem! Returning to main menu.")
            break
        elif polytechnic_input == 'exit':
            sys.exit()
        else:
            print("Please enter yes, no, or exit.")