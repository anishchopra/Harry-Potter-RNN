from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import LSTM
from keras.optimizers import RMSprop
import numpy as np
import random
import sys

from constants import *

phrases = []
next_chars = []

# generate all the windows in the text
for i in range(len(text) - window_size):
    phrases.append(text[i:i+window_size])
    next_chars.append(text[i+window_size])

# create training data
x = np.zeros((len(phrases), window_size, 1), dtype='bool')
y = np.zeros((len(phrases), len(chars)), dtype='bool')

for i,phrase in enumerate(phrases):
    for j,char in enumerate(phrase):
        x[i,j,0] = char_indices[char]

    y[i,char_indices[next_chars[i]]] = 1

x = x / float(len(chars))

print "Finished creating training data"
print "Building model..."

# build model
model = Sequential()
# by setting stateful=True, the state of the layer will preserved between batches
model.add(LSTM(128, input_shape=(window_size, 1), stateful=False))
model.add(Dense(len(chars)))
model.add(Activation('softmax'))

optimizer = 'adam'
model.compile(loss='categorical_crossentropy', optimizer=optimizer)

print "Finished building model"
print "Starting training..."

for i in range(300):
    print "Epoch %d" % (i+1)

    model.fit(x, y, nb_epoch=1, batch_size=batch_size, verbose=2, shuffle=False)

    model.save(model_file)
    model.reset_states()



