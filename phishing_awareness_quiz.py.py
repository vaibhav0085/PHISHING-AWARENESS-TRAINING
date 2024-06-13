# Phishing Awareness Quiz Program

# Introduction message
def introduction():
    print("Welcome to the Phishing Awareness Quiz!")
    print("This quiz will help you recognize and avoid phishing attacks.")
    print("You will be presented with various scenarios and asked to determine if they are phishing attempts.")
    print("Let's get started!\n")

# List of quiz questions and options
questions = [
    {
        "question": "You receive an email from your bank asking you to click a link to verify your account details. The email looks legitimate but the link's URL is suspicious. What should you do?",
        "options": [
            "A. Click the link and enter your details to verify your account.",
            "B. Ignore the email and delete it.",
            "C. Contact your bank using the phone number on their official website to verify the email.",
            "D. Forward the email to friends to see if they received it too."
        ],
        "correct": "C"
    },
    {
        "question": "An email from a well-known online store offers a great deal on a popular item. To claim the offer, you need to enter your personal information. What should you do?",
        "options": [
            "A. Enter your information quickly to get the deal.",
            "B. Check the sender's email address and look for spelling mistakes or unusual URLs.",
            "C. Delete the email immediately.",
            "D. Reply to the email asking for more details."
        ],
        "correct": "B"
    },
    {
        "question": "You receive a text message from an unknown number claiming you've won a prize and asking you to click a link to claim it. What should you do?",
        "options": [
            "A. Click the link to claim your prize.",
            "B. Respond to the message asking for more information.",
            "C. Report the message as spam and delete it.",
            "D. Forward the message to your friends."
        ],
        "correct": "C"
    },
    {
        "question": "A coworker sends you an email with an attachment labeled 'Important'. The email seems out of character for them. What should you do?",
        "options": [
            "A. Open the attachment immediately.",
            "B. Reply to the email asking if they meant to send the attachment.",
            "C. Ignore the email.",
            "D. Verify with your coworker through a different communication method (phone, in-person) before opening the attachment."
        ],
        "correct": "D"
    },
    {
        "question": "You receive a phone call from someone claiming to be from your IT department asking for your password to fix an issue. What should you do?",
        "options": [
            "A. Provide your password since they need it to fix the issue.",
            "B. Hang up and report the call to your actual IT department.",
            "C. Ask the caller for their contact details.",
            "D. Ignore the call."
        ],
        "correct": "B"
    }
]

# Function to conduct the quiz
def quiz():
    score = 0

    for i, q in enumerate(questions):
        print(f"Question {i + 1}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Your answer (A/B/C/D): ").upper()
        
        if answer == q["correct"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['correct']}.\n")
    
    print(f"Quiz completed! Your score: {score}/{len(questions)}")
    print("Thank you for participating in the Phishing Awareness Quiz! Stay vigilant and safe online.")

# Main function to run the program
def main():
    introduction()
    quiz()

# Run the program
if __name__ == "__main__":
    main()
