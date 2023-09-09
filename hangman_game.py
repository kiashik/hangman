"""
Name: Ashik Islam
Project: Hangman
"""
from hangman_functions import*

#rules
print("Please play the following HAGNMAN game according to these rules:\
	\n1. No world with repeating letters are allowed.\
	\n2. No sentences or pharses with spaces in between is allowed.\
	\n3. Six attempts allowed.")

begin = input("Proceed(y) or quit(n): ")
if begin == 'n':
	quit()
elif begin == 'y':
	print()


game_word = getWord() #returns word from user as char in a list and len(word)
print("The game word has",len(game_word[0]), "characters."
	"\n ")

progress =["Game word:"]
for c in game_word[0]:
	progress.append("_")
print(" ".join(progress))



fails = 0
guess = 0
already_guessed=["Wrong Guesses:"]
displyStatus(guess)
print("--------------------------------------")
while fails < 6:
	if progress[1:]==game_word[0]:
		print("YOU SAVED ME!! THANK YOU, FART FACE!")
		victory()
		quit()

	attempts_left= 6 - fails	
	print("Attempts left:", attempts_left)
	guess = getCharacter() #returns character as a string to test
	test = writtenStatus(guess, game_word[0]) #returns correct_guess, wrong_guess or False(already guessed).['Game Word:', 'w', '_', '_', '_']
	

	if test[0] == "Game Word:":
		for i in range(1, len(test)):
			if test[i]== guess:
				progress[i]=guess
		print("Yay! You got that right.", " ".join(progress))
	elif test[0] == "Wrong Guess:" and test[1] in already_guessed:
		print("You already", test[1], "tried that.", " ".join(already_guessed))
	elif test[0] == "Wrong Guess:":
		already_guessed.append(guess)
		print("Oops, try again.", " ".join(already_guessed))
		fails+=1
	displyStatus(fails)	
	print("--------------------------------------")

if fails == 6:
	print("Attempts left:", 0)
	print ("YOU FAILLED TO SAVE ME! DUMBSHIT!!!")
