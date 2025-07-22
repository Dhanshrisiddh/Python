# Simple KBC Game in Python
# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language
# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end now append three random characters at the starting and the end else: simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it else: remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

# Each question is a dictionary with the question, options and correct answer
questions = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "2. Who is known as the Father of the Nation?",
        "options": ["A. Nehru", "B. Bhagat Singh", "C. Mahatma Gandhi", "D. Sardar Patel"],
        "answer": "C"
    },
    {
        "question": "3. What is the national animal of India?",
        "options": ["A. Lion", "B. Elephant", "C. Tiger", "D. Leopard"],
        "answer": "C"
    }
]

# Prize money for each correct answer
prizes = [1000, 5000, 10000]

print("🎉 Welcome to Kaun Banega Crorepati 🎉")
print("Let's start the game!\n")

# Loop through each question
for i in range(len(questions)):
    q = questions[i]
    print(q["question"])
    
    # Display options
    for option in q["options"]:
        print(option)
    
    # Take user input
    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    # Check if the answer is correct
    if user_answer == q["answer"]:
        print(f"✅ Correct! You won ₹{prizes[i]}\n")
    else:
        print("❌ Wrong answer!")
        print(f"The correct answer was: {q['answer']}")
        print("Thank you for playing!")
        break
else:
    print("🏆 Congratulations! You answered all questions correctly!")

