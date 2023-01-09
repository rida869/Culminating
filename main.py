import tkinter as tk
import random
# Create the main window
window = tk.Tk()
#window.geometry("800x600")

questions = [
    ("What was the cause of World War II?", "The aggressive actions of Nazi Germany, led by Adolf Hitler"),
    ("Who was the leader of the Soviet Union during World War II?", "Joseph Stalin"),
    ("Which country was not one of the Allied Powers?", "Italy"),
    ("What was the code name for the operation to invade Normandy?", "D-Day"),
    ("What was the largest and deadliest war in human history?", "World War II")
]

def ask_question():
    # Select a random question
    question = random.choice(questions)
    # Extract the question and answer from the tuple
    question_text, answer = question
    # Display the question to the user
    label.config(text=question_text)
    # Get the user's answer
    user_answer = entry.get()
    # Check if the user's answer is correct
    if user_answer.lower() == answer.lower():
        # Display a message indicating that the answer is correct
        result_label.config(text="Correct!")
        return True
    else:
        # Display a message indicating that the answer is incorrect
        result_label.config(text="Incorrect. The correct answer is: " + answer)
        return False

def start_quiz():
    # Reset the quiz
    global score
    score = 0
    global start_time
    start_time = time.time()
    # Display the first question
    ask_question()

# Create a label to display the question
label = tk.Label(window)
label.pack()
# Select a random question from the list
question = random.choice(questions)

# Extract the question text from the tuple
question_text = question[0]

# Update the text of the label
label.config(text=question_text)


# Create an entry to accept the user's answer
entry = tk.Entry(window)
entry.pack()

# Create a button to submit the answer
button = tk.Button(window, text="Submit", command=ask_question)
button.pack()

# Create a label to display the result
result_label = tk.Label(window)
result_label.pack()

# Create a label to display the score
score_label = tk.Label(window)
score_label.pack()

# Create a label to display the elapsed time
time_label = tk.Label(window)
time_label.pack()

window.mainloop()
