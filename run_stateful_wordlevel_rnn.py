from keras.models import load_model
import numpy as np
import random

from constants import *

window_size = 1

# number of words to generate
num_words = 100

model = load_model('stateless_wordlevel_hp_rnn-01-6.7316.hdf5')

random_start = random.randint(0,len(text_words)-window_size-1)

# select a random phrase from the text to use as a seed
seed_text = text_words[random_start:random_start+window_size]

print ' '.join(seed_text)

seed = [word_indices[c] for c in seed_text]

output_text = ""

for _ in range(num_words):
	seed_value = np.reshape(seed, (1, window_size, 1))
	seed_value = seed_value / float(len(words))

	# Generate a prediction on the seed value
	prediction = model.predict(seed_value)
	index = np.argmax(prediction)

	predicted_word = indices_words[index]
	output_text += predicted_word + ' '

	# Add the predicted character to the seed and slide the window over
	seed.append(index)
	seed = seed[1:]

print output_text



