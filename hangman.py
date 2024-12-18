import random
liste=["red","yellwo","brwon","blue","orange","green","white","purple"]
random_liste=random.choice(liste)
print(" color word guessing game ")
user_guesses=""
chances=5
while chances >0:
    wrong_guess=0
    for ch in random_liste:
        if ch in user_guesses:
         print(ch, end = "")
        else:
         wrong_guess+=1
         print("_",end = "")
    if wrong_guess==0:
       print("\nCongrats.you won.the color is",random_liste)
       break
    guess=input("\n a guess")
    user_guesses+=guess
    if guess not in random_liste:
       chances-=1
       print("wrong.you have{chances}more chances")
       if chances ==0:
          print("game over.you lose.the word is",random_liste)

