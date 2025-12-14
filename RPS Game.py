import random

# Initialize scores
round_num = 1
user_wins = 0
computer_wins = 0
ties = 0

print("🎮 Welcome to Rock-Paper-Scissors Game! 🎮")
print("="*50)

while True:
    item_list = ["Rock", "Paper", "Scissor"]
    
    print(f"\n🔄 ROUND {round_num}")
    print("-"*30)
    
    # Get user input
    user_choice = input("Enter your move (Rock, Paper, Scissor): ").capitalize()
    
    # Validate input
    if user_choice not in item_list:
        print("Invalid choice! Please enter Rock, Paper, or Scissor.")
        continue
    
    # Computer makes choice
    comp_choice = random.choice(item_list)
    
    print(f"\n🎯 Your choice: {user_choice}")
    print(f"💻 Computer choice: {comp_choice}")
    
    # Determine winner
    if user_choice == comp_choice:
        print("🤝 Result: TIE! Both choose same.")
        ties += 1
        winner = "None"
        loser = "None"
    elif user_choice == "Rock":
        if comp_choice == "Paper":
            print("📄 Paper covers Rock = Computer wins!")
            winner = "Computer"
            loser = "You"
            computer_wins += 1
        else:  # Scissor
            print("🪨 Rock smashes Scissor = You win!")
            winner = "You"
            loser = "Computer"
            user_wins += 1
    elif user_choice == "Paper":
        if comp_choice == "Rock":
            print("📄 Paper covers Rock = You win!")
            winner = "You"
            loser = "Computer"
            user_wins += 1
        else:  # Scissor
            print("✂️ Scissor cuts Paper = Computer wins!")
            winner = "Computer"
            loser = "You"
            computer_wins += 1
    else:  # user_choice == "Scissor"
        if comp_choice == "Rock":
            print("🪨 Rock smashes Scissor = Computer wins!")
            winner = "Computer"
            loser = "You"
            computer_wins += 1
        else:  # Paper
            print("✂️ Scissor cuts Paper = You win!")
            winner = "You"
            loser = "Computer"
            user_wins += 1
    
    # Display winner and loser
    if winner != "None":
        print(f"🏆 Winner: {winner}")
        print(f"😞 Loser: {loser}")
    
    # Display summary
    print(f"\n📊 Round {round_num} Summary:")
    print(f"   Winner: {winner if winner != 'None' else 'No one - Tie'}")
    print(f"   Loser: {loser if loser != 'None' else 'No one - Tie'}")
    
    # Display overall score
    print(f"\n📈 OVERALL SCORE (after {round_num} rounds):")
    print(f"   Your wins: {user_wins}")
    print(f"   Computer wins: {computer_wins}")
    print(f"   Ties: {ties}")
    
    # Ask to continue
    print("\n" + "="*50)
    play_again = input("Play another round? (yes/no): ").lower()
    
    if play_again in ['no', 'n']:
        # Final results
        print("\n" + "="*50)
        print("🎯 FINAL RESULTS")
        print("="*50)
        print(f"Total rounds played: {round_num}")
        print(f"Your total wins: {user_wins}")
        print(f"Computer total wins: {computer_wins}")
        print(f"Total ties: {ties}")
        
        # Determine overall winner
        if user_wins > computer_wins:
            print(f"\n🎉🎉 CONGRATULATIONS! You are the overall WINNER! 🎉🎉")
            print(f"   You won {user_wins} out of {round_num} rounds!")
        elif user_wins < computer_wins:
            print(f"\n💻 Computer is the overall WINNER!")
            print(f"   Computer won {computer_wins} out of {round_num} rounds.")
        else:
            print(f"\n🤝 It's an overall DRAW!")
            print(f"   Both won {user_wins} rounds each.")
        
        print("\n👋 Thanks for playing! Goodbye!")
        break
    
    round_num += 1