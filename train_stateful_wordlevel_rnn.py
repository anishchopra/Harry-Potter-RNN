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

window_size = 1
batch_size = 1

x_data = []
y_data = []

# generate all the windows in the text
for i in range(len(text_words) - window_size):
    phrase = text_words[i:i+window_size]
    next_word = text_words[i+window_size]

    x_data.append([word_indices[w] for w in phrase])
    y_data.append(word_indices[next_word])

num_phrases = len(x_data)

# create training data
x = np.reshape(x_data, (num_phrases, window_size, 1))
y = np_utils.to_categorical(y_data)

# normalize
x = x / float(len(words))

print "Finished creating training data"
print "Building model..."

# build model
model = Sequential()
# by setting stateful=True, the state of the layer will preserved between batches
model.add(LSTM(256, batch_input_shape=(batch_size, window_size, 1), stateful=True, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(256))
model.add(Dropout(0.2))
model.add(Dense(len(words)))
model.add(Activation('softmax'))

optimizer = 'adam'
model.compile(loss='categorical_crossentropy', optimizer=optimizer)

class EndEpochCallback(callbacks.Callback):
	def on_epoch_end(self, epoch, logs):
		os.system('git add *')
		os.system('git commit -m "adding new models"')
		os.system('git push origin master')
		
push_callback = EndEpochCallback()


# define the checkpoint
filepath="stateful_wordlevel_hp_rnn-{epoch:02d}-{loss:.4f}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint, push_callback]

print "Finished building model"
print "Starting training..."

model.fit(x, y, nb_epoch=60, batch_size=batch_size, verbose=2, shuffle=False, callbacks=callbacks_list)