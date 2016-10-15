# Harry-Potter-RNN
A recurrent neural network that was trained using the entire text of "Harry Potter and the Goblet of Fire" to generate new Harry Potter text.

I'm still training this and experimenting with different architectures. Here is some output from a partially trained recurrent neural network (stateless_charlevel_hp_rnn-03-1.7017.hdf5) that takes predicts characters one at a time, using a seed text of 100 characters (with some autocorrect applied):

SEED TEXT:
ought of this."
fred, george, and lee ignored her.
"ready?"  fred said to the other two, quivering w


PREDICTED TEXT:
th his face was a horrible of the sare of the sare of the sare of the wand was a horrible of the sa



SEED TEXT:
the staff table.  there was definitely no new face there.
"maybe they couldn't get anyone!"  said he


PREDICTED TEXT:
rmione, and Hermione was staring at him i was a horrible was a cont of the way the dorrarc of the



SEED TEXT:
opping noise, and mr. weasley appeared out of thin air at george's shoulder.  he was looking angrier


PREDICTED TEXT:
ly and said and he was still the Soo of the sare of the sare of the sare of the sare of the goblet o



SEED TEXT:
ear the creak of a stair or the swish of a cloak?  and then he jumped slightly as he heard his cousi


PREDICTED TEXT:
e of the sare of the sare of the sare of the sare of the sare of the sare of the way the dormant of

### If attempting to train this on your own computer, I highly reccommend that you use a GPU, as recurrent neural networks take a long time to train. 
