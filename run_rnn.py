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

model = load_model(model_file)

with open(source_file, 'r') as f:
	text = f.read()

random_start = random.randint(0,len(text)-window_size-1)
random_start = 0

# select a random phrase from the text to use as a seed
seed_text = text[random_start:random_start+window_size]

print seed_text

seed_value = np.zeros((window_size, 1))

for i,char in enumerate(seed_text):
	seed_value[i][0] = char_indices[char]

seed_value /= float(len(chars))

output_text = ""

for _ in range(num_chars):
	seed_value = seed_value.reshape((1, window_size, 1))

	# Generate a prediction on the seed value
	prediction = model.predict(seed_value)[0]
	index = np.argmax(prediction)
	predicted_char = indices_char[index]
	output_text += predicted_char

	seed_value = seed_value.reshape((window_size, 1))

	# Add the predicted character to the seed and slide the window over
	new_value = np.zeros((1,1))
	new_value[0][0] = index
	new_value /= float(len(chars))
	seed_value = np.append(seed_value[1:], new_value)

print output_text

with open(output_file, 'w') as f:
	f.write(output_text)



