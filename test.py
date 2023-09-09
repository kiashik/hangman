def writtenStatus(character, word): #knows status of how many guesses left and what letters are taken. returns list of chatacters taken. and charters used in the world.
	#returns correct_guess, wrong_guess or False(already guessed).
	cha=character.lower()
	correct_guess = ["Game Word:"]
	wrong_guess = ["Wrong Guess:"]

	for c in word:
		correct_guess.append("_")
	print("aa", correct_guess)

	for j in range(len(word)):
		for i in range(len(word)): #if cha is correct, add to this list and remove placeholder('_')
			if cha == word[i]:
				correct_guess[i+1]=cha
				print("cor", correct_guess)
				return correct_guess
		if cha not in wrong_guess:
			wrong_guess.append(cha)
			return wrong_guess
		else:
			return (False, cha)
#################################

print(writtenStatus('ih', 'word'))