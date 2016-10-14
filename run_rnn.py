from keras.models import load_model
import numpy as np
import random

from constants import *

def printSeedValue(seed_value):
	text = ""
	for v in seed_value[0]:
		text += indices_char[int(v[0]*float(len(chars)))]
	print text

# number of characters to generate
num_chars = 1000

model = load_model('stateful_hp_rnn-16-2.5325.hdf5')

random_start = random.randint(0,len(text)-window_size-1)

# select a random phrase from the text to use as a seed
seed_text = text[random_start:random_start+window_size]

print seed_text

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

print output_text

with open(output_file, 'w') as f:
	f.write(output_text)



