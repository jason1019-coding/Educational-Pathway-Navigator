def user_input():
    while True:
        try:
            user_input = input("What is your child's current age(or 'exit' to quit): ")
            if user_input.lower() == 'exit':
                print("Exiting the program.")
                break
            number = int(user_input)
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
