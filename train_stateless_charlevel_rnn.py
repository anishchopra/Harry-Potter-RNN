from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint
import numpy as np
import random
import sys

from constants import *

window_size = 100
batch_size = 32

x_data = []
y_data = []

# generate all the windows in the text
for i in range(len(text) - window_size):
    phrase = text[i:i+window_size]
    next_char = text[i+window_size]

    x_data.append([char_indices[c] for c in phrase])
    y_data.append(char_indices[next_char])

num_phrases = len(x_data)

# create training data
x = np.reshape(x_data, (num_phrases, window_size, 1))
y = np_utils.to_categorical(y_data)

# normalize
x = x / float(len(chars)) 

print "Finished creating training data"
print "Building model..."

# build model
model = Sequential()

model.add(LSTM(256, input_shape=(window_size, 1), stateful=False, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(256))
model.add(Dropout(0.2))
model.add(Dense(len(chars)))
model.add(Activation('softmax'))

optimizer = 'adam'
model.compile(loss='categorical_crossentropy', optimizer=optimizer)


# define the checkpoint
filepath = "stateless_charlevel_hp_rnn-{epoch:02d}-{loss:.4f}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]

print "Finished building model"
print "Starting training..."

model.fit(x, y, nb_epoch=100, batch_size=batch_size, verbose=2, shuffle=False, callbacks=callbacks_list)



