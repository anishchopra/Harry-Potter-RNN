from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import LSTM
from keras.optimizers import RMSprop
import numpy as np
import random
import sys

source_file = 'Harry Potter and the Goblet of Fire.txt'
window_size = 20
batch_size = 1
model_file = 'harry_potter_rnn.h5'

with open(source_file, 'r') as f:
    text = f.read()

chars = sorted(list(set(text)))

char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))

phrases = []
next_chars = []

# generate all the windows in the text
for i in range(len(text) - window_size):
    phrases.append(text[i:i+window_size])
    next_chars.append(text[i+window_size])

# create training data
x = np.zeros((len(phrases), window_size, len(chars)), dtype='bool')
y = np.zeros((len(phrases), len(chars)), dtype='bool')

for i,phrase in enumerate(phrases):
    for j,char in enumerate(phrase):
        x[i,j,char_indices[char]] = 1

    y[i,char_indices[next_chars[i]]] = 1

print "Finished creating training data"
print "Building model..."

model = Sequential()
model.add(LSTM(128, batch_input_shape=(batch_size, window_size, len(chars)), stateful=True))
model.add(Dense(len(chars)))
model.add(Activation('softmax'))

optimizer = RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)

print "Finished building model"
print "Starting training..."

for i in range(300):
    print "Epoch %d" % (i+1)

    model.fit(x, y, nb_epoch=1, batch_size=batch_size, verbose=2, shuffle=False)

    model.save(model_file)
    model.reset_states()



