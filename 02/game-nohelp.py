#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH
import numpy.random as rd 

NUM_LETTERS = 7


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)

def draw_letters(num_letters):
	letters = []
	for _ in range(num_letters):
		idx = rd.randint(0, len(POUCH))
		letters.append(POUCH[idx])
		POUCH.remove(POUCH[idx])
	return letters

def is_valid(drawn_letters, word):
	cache = [x for x in drawn_letters]
	for w in word:
		if not w in cache: return False
		cache.remove(w)
	return True


def validate_entry(drawn_letters, word):
	best = {'word': '', 'score': 0}	
	valid = False
	word_lower = word.lower()
	for w in DICTIONARY:
		if w == word_lower: 
			valid = True
		w_upper = w.upper()
		if is_valid(drawn_letters, w_upper):
			score = calc_word_value(w_upper)
			if score > best['score']:
				best['word'] = w_upper
				best['score'] = score

	if not is_valid(drawn_letters, word): valid = False
	return valid, best

def main():
	drawn_letters = draw_letters(NUM_LETTERS)
	print(drawn_letters)
	entry = input('Please input your entry: ')
	valid = 'not valid'
	isValid, best = validate_entry(drawn_letters, entry)
	score = 0
	if isValid: 
		score = calc_word_value(entry.upper())
		valid = 'valid'
	print('your entry [%s] is %s\n' % (entry, valid))
	print('the best result is %s with score %d\n' % 
		(best['word'], best['score']))
	scorePerc = float(score) / best['score'] * 100
	print('your score is: %d/%d = %.2f%%\n' % 
		(score, best['score'], scorePerc))

if __name__ == "__main__":
    main()
