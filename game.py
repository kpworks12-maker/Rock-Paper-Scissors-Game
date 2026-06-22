import random
rock = '''   
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images = [rock, paper, scissors]


response = int(input("enter your choice:"))
print(images[response])
comp_response = random.randint(0,2)
print(f"computer chose {images[comp_response]}")

if response == 0 and comp_response == 2:
    print("you win")
elif response == 2 and comp_response == 0:
    print("you lose")
elif response >= 3 or response < 0:
    print("invalid choice")
elif comp_response > response:
    print("you lose")
elif comp_response < response:
    print("you win")
elif comp_response == response:
    print("it's a draw")