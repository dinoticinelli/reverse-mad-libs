# The following are dictionaries to establish initial values for blank spaces and their corresponding correct answers.
mystery_words = {"blank 1": "___1___", "blank 2": "___2___", "blank 3": "___3___", "blank 4": "___4___", "blank 5": "___5___", "blank 6": "___6___", "blank 7": "___7___", "blank 8": "___8___"}
correct_answers = {"___1___": "sun", "___2___": "wet", "___3___": "house", "___4___": "day", "___5___": "two", "___6___": "wish", "___7___": "play", "___8___": "nothing"}

# The following are strings* corresponding to difficulty levels to be passed through the level_difficulty function. *strings taken from "The Cat in the Hat" by Dr. Seuss, copyright Dr. Seuss Enterprises
level_easy = 'The {blank 1} did not shine. It was too {blank 2} to play. So we sat in the {blank 3} all that cold, cold, {blank 2} {blank 4}.'
level_medium = 'The {blank 1} did not shine. It was too {blank 2} to play. So we sat in the {blank 3} all that cold, cold, {blank 2} {blank 4}. I sat there with Sally. We sat there, we {blank 5}. And I said, "How I {blank 6} we had something to do!"'
level_hard = 'The {blank 1} did not shine. It was too {blank 2} to play. So we sat in the {blank 3} all that cold, cold, {blank 2} {blank 4}. I sat there with Sally. We sat there, we {blank 5}. And I said, "How I {blank 6} we had something to do!" Too {blank 2} to go out and too cold to {blank 7} ball. So we sat in the {blank 3}. We did {blank 8} at all.'

# Displays a greeting for the player and a prompt to select a difficulty level.
user_prompt = "\n" + "It's a Mad Mad Mad Libs game! Choose your path >> easy, medium or hard? "
user_choice = raw_input(user_prompt)

# Returns the mad libs string corresponding to the difficulty level given by user_choice.
def level_difficulty(user_choice):
	if user_choice == "easy":
		return level_easy
	elif user_choice == "medium":
		return level_medium
	elif user_choice == "hard":
		return level_hard

# Displays the current mad libs statement.
def display_ml(mystery_words):
	current_ml = level_difficulty(user_choice).format(**mystery_words)
	print "\n" + current_ml + "\n"
	return current_ml

# Returns the next "blank" from mystery_words appearing in the mad lib statement.
def remaining_blanks(word, mystery_words):
	for blank in mystery_words.values():
		if blank in word:
			return blank
	return None

# Returns the "key" corresponding to the given "blank" in mystery_words so its value can be updated later.
def update_mystery_words(replacement, mystery_words):
	for key in mystery_words.keys():
		if mystery_words[key] == replacement:
			replacement = key
			return replacement

def play_game(ml_string, mystery_words):
	ml_string = display_ml(mystery_words)
	ml_string = ml_string.split()
	for word in ml_string:
		replacement = remaining_blanks(word, mystery_words)
		if replacement != None:
			user_input = raw_input("Type in a word for " + replacement + ": ")
			while user_input not in correct_answers[replacement]:
				user_input = raw_input("Almost!! Try " + replacement + " again: ")
			else:	
				print "Yes!"
				mystery_words[update_mystery_words(replacement, mystery_words)] = user_input # Updates mystery_words
				display_ml(mystery_words)
	print "Congrats! You conquered this Mad Libs." + "\n"

play_game(level_difficulty(user_choice), mystery_words)
