Educational Pathway Navigator


What is this project?
Choosing a school pathway is easily one of the biggest milestones for any student in Singapore. Yet, every single year, so many students and parents feel completely lost trying to decode the massive wall of options, requirements, and cut-off points. We built this simple terminal tool to change that. We wanted to create a straightforward, stress-free space where youth can actually understand the routes open to them and make choices they feel confident about.

What it can do
Step-by-step menu system: Instead of overwhelming the user with choices, the app uses a step-by-step menu system. It first asks for the current education level, handles that input, and then dynamically populates a secondary menu tailored specifically to that choice

Error Handling:
Incorporates try-except blocks to manage network failures or invalid HTTP responses, preventing terminal crashes if the API is temporarily unavailable.
Incorporates .lower() to forces input to the lowercased. 
Handles Typos or invalid selections. If a user accidentally enters a number or letter that isn't on the menu, the terminal catches it, displays a warning, and prompts user to try again without crashing the program


How to Run
What you need
Just regular Python 3 and the requests library so the app can talk to the live API.

Step 1: Install the network library
Pop open your terminal and run this quick command:

Bash
pip install requests
Step 2: Fire it up!
Navigate to your project folder and start the program with:

Bash
python Main.py
📁 File Map
Plaintext
├── Main.py                    # The heart of the app (handles the main menus and user inputs)
├── primary_sch.py             # Primary school tracks and eligibility logic
├── secondary_sch.py           # Secondary school streams and structures
├── junior_college.py          # Junior College requirements and paths
├── polytechnic.py             # Polytechnic course frameworks
└── millennia_institute.py     # Specialized subject choices for MI
💭 Reflection
The hardest hurdle we faced
The biggest headache we faced was definitely wrestling with the logic inside our main menu loop. It sounds pretty simple on paper, but getting the conditional statements to behave perfectly across every scenario turned out to be a massive game of trial and error. We had to carefully map out how the code routes user inputs so that everything flows smoothly without hitting a dead end.

For starters, we had to make sure that when a user types exit or chooses to quit, the program triggers a clean break and shuts down gracefully. But at the same time, we had to do the exact opposite for typos and invalid numbers. If a parent or student accidentally hits the wrong key, we did not want the app to crash or exit out on them. Instead, we needed the loop to catch the mistake, print a friendly warning, and smoothly reset so they could try again. Balancing when to kill the loop and when to keep it running took a lot of careful debugging, especially since we also had to pause the screen so people actually had time to read the text before it refreshed.

If we had two more weeks, we would add...
A Built-in COP Calculator: We’d love to let students type their actual O-Level L1R5 or ELR2B2 scores right into the prompt to instantly filter out schools they don't qualify for.

Contextual Searching: We want to merge the search tool inside the pathways, so parents can filter for specific schools within their chosen category (like searching specifically for Science JCs in the North).
