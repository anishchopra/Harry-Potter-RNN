source_file = 'Harry Potter and the Goblet of Fire.txt'
window_size = 100
batch_size = 128
model_file = 'harry_potter_rnn3.h5'
output_file = 'harry_potter_text.txt'

with open(source_file, 'r') as f:
    text = f.read()
    text = text.lower()
    text = text[:int(len(text)*0.2)]

print "Text length: %d" % len(text)

chars = sorted(list(set(text)))

char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))