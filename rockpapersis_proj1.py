import random
user_inp=input("Enter 0 for paper 1 for rock 2 for scissors:  ")
user=int(user_inp)
comp_list=[0,1,2]
comp=random.choice(comp_list)
print(comp)
if user>2 or user<0:
    print("Enter within the range")
else:
 if user==comp:
    print("It's a draw")
 elif user==2 and comp==0:
    print("You win")
 elif user==0 and comp==2:
    print("You lose")
 elif user<comp:
    print("You win")
 elif user>comp:
    print("You lose")
