from helpers import load_words, filter_words, get_frequency_dist, letterwise_guess

# state example: array of [('S', 'c'), ('T', 'w'), ('E', 'n')]
# c = correct spot, w = in word but wrong spot, n = not in word
file_name = 'words.txt'
possible_words = load_words(file_name)
freq_dist = get_frequency_dist(possible_words)
first_guess = None
stabilized_letters = {}
for i in range(6):
	if i == 0:
		recommended = letterwise_guess(possible_words, freq_dist)
		print(f'\nTo eliminate the most words, guess {recommended}')
	elif i == 1:
		recommended = letterwise_guess(possible_words, freq_dist, True, first_guess)
		print(f'\nTo eliminate the most words, guess {recommended}')

	guess = input('\nPlease guess a word: ').lower()
	result = input('Is the word you guessed correct? (y/n) ')
	if result == 'y':
		print('nice')
		break
	if i == 0:
		first_guess = guess
	print('What were the results that Wordle gave you?')
	print('Key: \'c\' = letter is in correct spot, \'w\' = letter is in the word but at the wrong spot, \'n\' = letter is not in the word')
	results = []
	for index,letter in enumerate(guess):
		prompt = f'What did you get for letter {letter}? '
		letter_result = input(prompt)
		if letter_result == 'c':
			if letter in stabilized_letters:
				stabilized_letters[letter].append(index)
			else:
				stabilized_letters[letter] = [index]
		results.append(letter_result)
	for index,result in enumerate(results):
		possible_words = filter_words(possible_words, index, guess[index], result, stabilized_letters)
	if len(possible_words) == 0:
		print('The word is not in the list that this application is using, sorry about that')
		break
	freq_dist = get_frequency_dist(possible_words)
	if i != 5:
		print('\nThank you. Here\'s all possible remaining words: ')
		print(possible_words)
	else:
		print('Better luck next time!')