source_file = 'Harry Potter and the Goblet of Fire.txt'
window_size = 20
batch_size = 1
model_file = 'harry_potter_rnn.h5'
output_file = 'new_harry_potter_text.txt'

with open(source_file, 'r') as f:
    text = f.read()

chars = sorted(list(set(text)))

char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))