from keras.models import load_model
import numpy as np
import random
from autocorrect import spell

from constants import *

window_size = 1

# number of characters to generate
num_chars = 100

model = load_model('stateful_charlevel_hp_rnn-01-2.5778.hdf5')

for _ in range(10):
	random_start = random.randint(0,len(text)-window_size-1)

	# select a random phrase from the text to use as a seed
	print "SEED TEXT:"
	seed_text = text[random_start:random_start+window_size]

	print seed_text
	print '\n'*2

	seed = [char_indices[c] for c in seed_text]

	output_text = ""

	for _ in range(num_chars):
		seed_value = np.reshape(seed, (1, window_size, 1))
		seed_value = seed_value / float(len(chars))

		# Generate a prediction on the seed value
		prediction = model.predict(seed_value)
		index = np.argmax(prediction)

		predicted_char = indices_char[index]
		output_text += predicted_char

		# Add the predicted character to the seed and slide the window over
		seed.append(index)
		seed = seed[1:]

	output_text = ' '.join([spell(word) for word in output_text.split()])
	print output_text

	print '\n'*4



