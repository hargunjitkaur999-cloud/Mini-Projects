#time to play rock paper scissors game

print("🎮 “Let’s gooo! Game time 🎮🔥”")

def rock_paper_scissorss_game():
       import random
#--------------------------------------------------------------------------------------------
                #messages for different outcomes
       computer_won_msgs = [
            "😭 Oopsie! Computer got lucky this time 💻🍀",
            "🤖 Beep boop! Computer wins 🤖✨",
            "🫠 Awww, computer stole the win 😔💻",
            "😤 Not fairrr 😤💻 Try again!",
            "🧠 Computer used big brain energy 🧠💻"
             ]
       you_won_msgs =[
            "🥳 Yayyy! You crushed it! 💪✨",
            "😎 Slayyy! You win this round 🔥🎉",
            "🏆 Winner vibes only 😌✨",
            "💃 You did THAT 💃💥",
            "🌟 Main character moment ✨🌟"
             ]
       invalid_msgs = [
            "🫣 Uh-oh! That's not a valid move 😅❌",
            "🤔 Rock, Paper, or Scissors only please ✂️📄",
            "😵 Oopsie! Try choosing properly 😵‍💫",
            "🚫 Nope nope! Try again 😄",
            "🐣 It's okay! Choose again cutie ✨"
            ] 
#--------------------------------------------------------------------------------------------
# game logic starts from here     
                                                                 
       choices=["rock","paper","scissors"]
       comp_choice=random.choice(choices)
       users_choice=input("enter your choice(rock,paper,scissors):").lower()
       if comp_choice==users_choice:
         print("Tie game! No one lost 🫶💫")
         print(f"computer's choice was {comp_choice} and your choice is {users_choice}")
       elif comp_choice=="rock" and users_choice=="paper":
         print(random.choice(you_won_msgs))
         print(f"computer's choice was {comp_choice} and your choice is {users_choice}")
       elif comp_choice=="rock" and users_choice=="scissors":
         print(random.choice(computer_won_msgs))
         print(f"computer's choice was {comp_choice} and your choice is {users_choice}")
       elif comp_choice=="paper" and users_choice=="rock":
         print(random.choice(computer_won_msgs))
         print(f"computer's choice was {comp_choice} and your choice is {users_choice}")
       elif comp_choice=="paper" and users_choice=="scissors":
         print(random.choice(you_won_msgs))
         print(f"computer's choice was {comp_choice} and your choice is {users_choice}")
       elif comp_choice=="scissors" and users_choice=="paper":
         print(random.choice(computer_won_msgs))
         print(f"computer's choice was {comp_choice} and your choice is {users_choice}")
       elif comp_choice=="scissors" and users_choice=="rock":
         print(random.choice(you_won_msgs))
         print(f"computer's choice was {comp_choice} and your choice is {users_choice}")
       elif users_choice  not in choices:
            print("invalid input")
       else:
         print(" No worries! See you next time ✨")

#--------------------------------------------------------------------------------------------
#game loop starts from here
     
while True:
    confirmation=input("DO you want to play ROCK-PAPPER-SCISSORS game ? yes/no :").lower()
    if confirmation=='yes':
       rock_paper_scissorss_game()
    else:
       print(" No worries! See you next time ✨")
       

    
        
    





