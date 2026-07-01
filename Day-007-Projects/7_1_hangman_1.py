#Part 1
import random
import hangman_words
import hangman_art


print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)

# chosen_word = random.randint(0,len(word_list)-1)
# print(word_list[chosen_word])


display = []
for letter in chosen_word:
    display.append("_")

#display = [" "] * len(chosen_word)

#for _ in range(len(chosen_word)):
    # display += "_"

print(display)

#or i can create a variable end_of_game = False

lives = 6
already_guess = []
# end_of_game = False

while True: # set this to while not end_of_game:

        guess = input("Guess a letter: ").lower()
        if guess in already_guess:
            print(f"You already guessed '{guess}'")
            continue

        already_guess.append(guess)

        print(f"Guessed letters: {', '.join(already_guess)}")

        

        iteration = 0
        for letter in chosen_word:
            if guess == letter: 
                # temp = chosen_word.find(letter)
                display[iteration] = guess
            iteration += 1
    
        
        if guess not in chosen_word:
             lives -= 1
             print(hangman_art.stage[6 - lives])
             if lives == 0:
                  print("You lose")
                  break

        print(f"{' '.join(display)}") 

        if "_" not in display:
             print("You win")
             break
        
             



    


    #change
    # if "_" not in display:
    #     end_of_game = True
    #     print("YOu win")

# for index,letter in enumerate(chosen_word):
#     if guess == letter:
#         display[index] = guess


        



