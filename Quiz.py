
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# -------------------------
def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------


questions={
    "Which of the following is the movie directed by Christopher Nolan:":"C",
    "What is the name of the theoretical spaceship which can achieve the speed of light:":"B",
    "On which Principle does airplane fly:":"D",
    "What is consider as a physical object in 4th dimension:":"C"
}

options=[["A. Fast & Furious","B. Pirates of the carribean","C. Interstellar","D. Avengers"],
         ["A.Fission sail","B.AlcubierreWarp Drive","C.Gravitational shielding","D.Nano electrokinetic thruster"],
         ["A.Mechanical force","B.Relativity","C.Archimedes' principle","D.Bernoulli's principle"],
         ["A.Light","B.Sound","C.Time","D.Gravity"]]

new_game()
while play_again():
    new_game()

print("Bye")
