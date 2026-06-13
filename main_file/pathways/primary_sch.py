primary_school_pathways = {
    "DSA": {
        "name": "Direct School Admission",
        "descrxiption": "Allows students to apply to secondary schools based on their talents and interests.",
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

def primary_school():
    primary_sch_input = input("Would like to know to about the different pathways primary school students can take other than just academics? (yes/no): ")
    for key, value in primary_school_pathways.items():
        print(f"{key}: {value['name']}")

    if primary_sch_input.lower() == 'yes':
        print("Here are the different pathways primary school students can take other than just academics:")
        for key, value in primary_school_pathways.items():
            print(f"{key}: {value['name']}")
    elif primary_sch_input.lower() == 'no':
        print("Would you like to know about the different pathways secondary school students can take other than just academics? (yes/no): ")
        