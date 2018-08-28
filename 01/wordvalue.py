from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as file:
    	return file.read().splitlines()


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    value = 0
    for w in word.upper():
    	try:
    		value += LETTER_SCORES[w]
    	except:
    		continue

    return value

def max_word_value(*args):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if len(args) == 0:
    	words = load_words()
    else:
    	words = args[0]

    maxVal = (0, '')
    for w in words:
    	curVal = calc_word_value(w)
    	if curVal > maxVal[0]:
    		maxVal = (curVal, w)

    return maxVal[1]

if __name__ == "__main__":
    pass # run unittests to validate
