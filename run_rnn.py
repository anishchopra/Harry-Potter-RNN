from keras.models import load_model
import numpy as np
import random

from constants import *

# number of characters to generate
num_chars = 1000

model = load_model(model_file)

with open(source_file, 'r') as f:
	text = f.read()

random_start = random.randint(0,len(text)-window_size-1)

# select a random phrase from the text to use as a seed
seed_text = text[random_start:random_start+window_size]

seed_value = np.zeros((window_size, len(chars)))

for i,char in enumerate(seed_text):
	seed_value[i][char_indices[char]] = 1

output_text = ""

for _ in range(num_chars):
	seed_value = seed_value.reshape((1, window_size, len(chars)))

	prediction = model.predict(seed_value)[0]
	index = np.argmax(prediction)
	predicted_char = indices_char[index]
	output_text += predicted_char

	seed_value = seed_value.reshape((window_size, len(chars)))

	new_value = np.zeros((1,len(chars)))
	new_value[0][index] = 1

	seed_value = np.append(seed_value[1:], new_value)

print output_text

with open(output_file, 'w') as f:
	f.write(output_text)



