"""
Name: Ashik Islam
Project: Hangman
"""

# what is the word?
def getWord(): #returns word from user as char in a list and len(word)
	inp_ = str(input("What word will you be playing for? ")).lower()
	word=[]

	for cha in inp_:
		word.append(cha)
	
	return [word, len(word)]

def getCharacter():
	#asks user for a char. returns character as a string
	char = str(input("What's your guess? ")).lower()
	return char

def writtenStatus(character, word): #knows status of how many guesses left and what letters are taken. returns list of chatacters taken. and charters used in the world.
	#returns correct_guess, wrong_guess or False(already guessed).
	cha=character.lower()
	correct_guess = ["Game Word:"]
	wrong_guess = ["Wrong Guess:"]

	for c in word:
		correct_guess.append("_")
	#print("aa", correct_guess)

	for j in range(len(word)):
		for i in range(len(word)): #if cha is correct, add to this list and remove placeholder('_')
			if cha == word[i]:
				correct_guess[i+1]=cha
				#print("cor", correct_guess)
				return correct_guess
		if cha not in wrong_guess:
			wrong_guess.append(cha)
			return wrong_guess
		

def displyStatus(num): #shows seven(0-6) steps hangman corresponing to the input
	head = "|"
	abdomen_arm = abdomen = "|" 
	legs = "|"

	if num == 1:
		head = "O      |"
	elif num == 2:
		head = "O      |"
		abdomen_arm = abdomen ="|      |"
	elif num == 3:
		head = "O      |"
		abdomen_arm = "/|      |"
		abdomen = "|      |" 
	elif num == 4:
		head = "O      |"
		abdomen_arm = "/|\\     |"
		abdomen ="|      |"
	elif num == 5:
		head = "O      |"
		abdomen_arm = "/|\\     |"
		abdomen ="|      |"
		legs = "/       |"
	elif num == 6:
		head = "O      |"
		abdomen_arm = "/|\\     |"
		abdomen ="|      |"		
		legs = "/ \\     |"
	
	print("{:^60}".format("________"))
	print("{:^60}".format("|      |"))

	print("{:>34}".format(head))
	print("{:>34}".format(abdomen_arm))
	print("{:>34}".format(abdomen))
	print("{:>34}".format(legs))

	print("{:>34}".format("|"))
	print("{:>34}".format("|"))
	print("{:>34}".format("|"))
	print("{:>36}".format("—————"))

def victory():
	print("{:^60}".format("________"))
	print("{:^60}".format("|      |"))

	print("{:>34}".format("|"))
	print("{:>34}".format("|"))
	print("{:>34}".format("|"))
	print("{:>34}".format("|"))

	print("{:>34}".format("\\O/     |"))
	print("{:>34}".format("|      |"))
	print("{:>34}".format("|      |"))
	print("{:>36}".format("/ \\    ————"))

