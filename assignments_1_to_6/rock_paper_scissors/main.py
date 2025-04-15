import random
print("Welcome to the Rock, Paper, Scissors Game!")
print("Enter 'r' for rock, 'p' for paper, and 's' for scissors.")
choices = ["rock", "paper", "scissors"]
user_score =  computer_score = 0
print("Let\'s play!")
while True:
    user_input = input("Enter your Rock, Paper, or Scissors choice: ").lower()
    if user_input == "q":
        print(f"Final score: You: {user_score} Computer: {computer_score}")
        print("Thanks for playing!")
        break
    if user_input not in choices:
        print("Invalid input. Please enter 'r' for rock, 'p' for paper, and 's' for scissors.")
        continue
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    if user_input == computer_choice:
        print("It's a tie!")
    elif (user_input == "rock" and computer_choice == "scissors") or \
         (user_input == "paper" and computer_choice == "rock") or \
         (user_input == "scissors" and computer_choice == "paper"):
        print("You win!")
        user_score += 1
    else:
        print("You computer wins!")
        computer_score += 1

print(f"Current score: You: {user_score} Computer: {computer_score}")    
    
            
    
    

