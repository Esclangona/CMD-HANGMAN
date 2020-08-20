######################
#CMD-HANGMAN
######################

import random


word_list = ["apple", "mobile", "telephone", "computer", "allegory", "betablocker"]


is_running = True
word_chosen = False
lives = 10
current_word = ""


while lives > 0 and is_running:

	if word_chosen == False:
		random_word = word_list[random.randrange(len(word_list))]
		current_word = list(random_word)
		in_list = list(random_word)
		for i in range(len(current_word)):
			current_word[i] = "_"
		word_chosen = True
	else:
		end_game = "".join(current_word) == random_word

		if end_game == True and is_running == True:
			print("The word is:", random_word)
			print("You win the game!")
			is_running = False
			break

		else:
			print("=" * 5 + " NEXT ROUND " + "=" * 5)
			
			print("Current word: " + " ".join(current_word))
			
			user_guess = input("Your guess?\n>> ")

			if (user_guess.isalpha() == True and len(user_guess)==1) or (user_guess == random_word): 
				for i in range(len(random_word)):
					if in_list[i] == user_guess:
						index = in_list.index(user_guess)
						in_list[i] = "_"
						current_word[index] = user_guess
					elif user_guess not in random_word:
						print("Wrong answer")
						lives = lives - 1
						print("lives", lives)
						break
					elif (user_guess == random_word):
						print("You win the game!")
						is_running = False
						break		

			elif len(user_guess)>1 and user_guess != random_word:
				print("You can only guess one letter at a time or the whole word.") 
			elif int(user_guess) != None:
				print("You need to write a letter not a number.")		
			

