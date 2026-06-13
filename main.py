def user_input():
    while True:
        try:
            user_input = input("What is your child's current level(or 'exit' to quit): ")
            if user_input.lower() == 'exit':
                print("Exiting the program.")
                break
            number = float(user_input)
            print(f"Based on the input, your child's current level is: {number}")
        except ValueError:
            print("Invalid input. Please enter a valid number or 'exit' to quit.")


class primary_school:
    def __init__(self, age):
        self.age = age
    
    if self.age >= 5 and self.age <= 11:
       primary_sch_input = input("Would like to know to about the different pathways primary school students can take other than just academics? (yes/no): ")
    if primary_sch_input.lower() == 'yes':
        print("One pathway would be Direct School Admission (DSA) which allows students to apply to secondary schools based on their talents and interests")
        
    elif primary_sch_input.lower() == 'no':
        print("No problem! If you have any questions in the future, feel free to ask.")
primary_school_pathways = {
    "DSA": {
        "name": "Direct School Admission",
        "description": "Allows students to apply to secondary schools based on their talents and interests.",
        "deadline": "Typically in the first half of the year",
        "eligibility": "Primary school students with exceptional talents in areas such as sports, arts, or academics."
        },
    "Full SBB": {
        "name": "Mainstream Secondary Pathway (Full SBB)",
        "description": "Students follow the standard curriculum and are assessed through national exams.",
        "eligibility": "Primary school students who meet the academic requirements for secondary school admission."
    },
    "IP Pathway": {
        "name": "The Integrated Programme (IP) Pathway",
        "description": "A 6-year program that combines the primary and secondary school curricula.",
        "deadline": "Typically in the first half of the year",
        "eligibility": "Primary school students who meet the academic requirements for the IP program."
    },
    "Specialised & Specialised Independent Schools Pathway": {
        "name": "Specialised & Specialised Independent Schools Pathway",
        "description": "Offers specialized education in areas such as arts, sports, or science.",
        "eligibility": "Primary school students with exceptional talents in specific areas who meet the admission"
    }


}
