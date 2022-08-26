# Return a list of words from a file
def load_words(file_name):
	lines = []
	with open(file_name) as f:
		for line in f.readlines():
			lines.append(line[:-1])
	lines = [line.lower() for line in lines]
	return lines

# c = correct spot, w = in word but wrong spot, n = not in word
def filter_words(words, index, letter, type, stabilized_letters):
	new_words = []
	for word in words:
		if type == 'c':
			if word[index] == letter:
				new_words.append(word)
		elif type == 'w':
			# if letter already stabilized somewhere else, make sure there's another
			if letter in stabilized_letters:
				count = 0
				for word_letter in word:
					if word_letter == letter:
						count += 1
				if count > len(stabilized_letters[letter]) and word[index] != letter:
					new_words.append(word)
			elif word[index] != letter and letter in word:
				new_words.append(word)
		else:
			# if letter stabilized somewhere else, still add if not anywhere else
			if letter in stabilized_letters:
				add = True
				other_indices = stabilized_letters[letter]
				for letter_ind, word_letter in enumerate(word):
					if letter_ind not in other_indices and word_letter == letter:
						add = False
						break
				if add:
					new_words.append(word)
			elif letter not in word:
				new_words.append(word)
	return new_words

# Get a frequency distribution of letters in certain spots of a word
def get_frequency_dist(words):
	last_weight = 0.01
	base = last_weight**(1/len(words))
	freq_dist = {}

	for word_ind,word in enumerate(words):
		for letter_ind, letter in enumerate(word):
			if letter not in freq_dist:
				freq_dist[letter] = [0 for i in range(5)]
			freq_dist[letter][letter_ind] += base ** word_ind

	return freq_dist

# Return the best guess based on the frequency distribution of certain letters
def letterwise_guess(words, freq_dist, distinctFromPrev=False, previous=None):
	best_score = 0.0
	for word in words:
		score = 0.0
		duplicateCount = 0
		found_letters = []
		for ind,letter in enumerate(word):
			score += freq_dist[letter][ind]
			if letter in found_letters:
				duplicateCount += 1
			elif distinctFromPrev and letter in previous:
				duplicateCount += 1
			else:
				found_letters.append(letter)
		score /= (duplicateCount + 1)
		if score > best_score:
			best_guess = word
			best_score = score
	return best_guess