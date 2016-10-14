source_file = 'Harry Potter and the Goblet of Fire.txt'
punctuation = set([',', '.', ':', "'", '"', ';', '~', '!', '/'])

with open(source_file, 'r') as f:
    text = f.read()
   
text = text.lower()
temp_text_words = text.split()

text_words = []
for word in temp_text_words:
	split_indices = []
	for i,c in enumerate(word):
		if c in punctuation:
			split_indices.append(i)

	last_i = 0
	for i in split_indices:
		text_words.append(word[last_i:i])
		text_words.append(word[i])
		last_i = i+1

	text_words.append(word[last_i:])

text_words = [x for x in text_words if x != ""]

print "Text length: %d" % len(text)
print "Number of words: %d" % len(text_words)

chars = sorted(list(set(text)))

print "Total unique chars: %d" % len(chars)

char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))

words = sorted(list(set(text_words)))

print "Total unique words: %d" % len(words)

word_indices = dict((w, i) for i,w in enumerate(words))
indices_words = dict((i, w) for i,w in enumerate(words))